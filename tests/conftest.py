import os

import pytest
import time
from appium import webdriver
import allure

from config import EnvConfig, DeviceConfig, TestConfig, Config


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="prod", help="Environment to run tests against"
    )
    parser.addoption(
        "--device-name",
        action="store",
        required=True,
        help="Running tests on specified device",
    )
    parser.addoption(
        "--build",
        action="store",
        default=0,
        help="Kobiton only. Running tests on specified build. By default takes latest build.",
    )


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def device_name(request):
    return request.config.getoption("--device-name")


@pytest.fixture(scope="session")
def build(request):
    return request.config.getoption("--build")


@pytest.fixture(scope="session")
def env_config(env, build):
    env_cfg = EnvConfig(env=env, build=build)
    return env_cfg


@pytest.fixture(scope="session")
def device_config(env_config, device_name):
    device_cfg = DeviceConfig(device_name=device_name, env_config=env_config)
    return device_cfg


@pytest.fixture(scope="module")
def test_config():
    test_cfg = TestConfig()
    return test_cfg


@pytest.fixture(scope="module")
def config(device_config, env_config, test_config):
    config = Config(
        env_config=env_config, device_config=device_config, test_config=test_config
    )
    return config


@pytest.fixture
def platform(config):
    return config.platform_name


@pytest.fixture(autouse=True)
def skip_by_platform(request, platform):
    if request.node.get_closest_marker("skip_platform"):
        if request.node.get_closest_marker("skip_platform").args[0] == platform:
            pytest.skip(
                "skipped on: {}".format(platform)
                + " - "
                + request.node.get_closest_marker("skip_platform").args[1]
            )


@pytest.fixture(scope="session")
def driver(device_config):
    run_location = device_config.run_location
    desired_caps = device_config.desired_capabilities

    raised = True
    seconds_tried = 0
    wait_time = 120
    driver = None

    try:

        while raised and seconds_tried <= wait_time:
            try:

                driver = webdriver.Remote(run_location, desired_caps)

                raised = False
                print("Webdriver: Done waiting for device: Device Obtained")

            except Exception as e:
                time.sleep(5)
                seconds_tried += 5
                print(e)
                print(
                    "Trying device again shortly. Currently waited: "
                    + str(seconds_tried)
                )

        if raised:
            print("Webdriver: Done waiting for device: device NOT obtained")
            raise

        yield driver

        driver.quit()

    except Exception as e:
        pytest.skip(f"Driver not able to be started. {e}", allow_module_level=True)


@pytest.fixture(autouse=True)
def allure_params():
    return


@pytest.fixture(autouse=True)
def allure_setup(driver, env_config, device_config):
    if "deviceGroup" in device_config.desired_capabilities:
        allure.dynamic.parent_suite(f"{device_config.device_name}")
        kobiton_session_id = driver.desired_capabilities.get("kobitonSessionId")
        kobiton_url = "https://portal.kobiton.com/sessions/" + str(kobiton_session_id)
        allure.dynamic.link(
            kobiton_url, name="Kobiton Link - " + str(device_config.build)
        )
    return


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode) as f:
                if "driver" in item.fixturenames:
                    web_driver = item.funcargs["driver"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))
