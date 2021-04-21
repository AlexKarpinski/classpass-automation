import pytest
import time
from appium import webdriver

from page_object.config import EnvConfig, DeviceConfig, TestConfig, Config


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="Environment to run tests against"
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
    if request.node.get_closest_marker('skip_platform'):
        if request.node.get_closest_marker('skip_platform').args[0] == platform:
            pytest.skip('skipped on: {}'.format(platform)+" - " +
                        request.node.get_closest_marker('skip_platform').args[1])


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

