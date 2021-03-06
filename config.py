import os

from desired_capabilities import DesiredCapabilities


class Config(object):
    def __init__(self, env_config, device_config, test_config):
        self.platform_name = device_config.platform_name
        self.platform_version = device_config.platform_version
        self.env = env_config.env
        self.test_scope = test_config.test_scope


class TestConfig(object):
    def __init__(self):
        self.full_name = os.getenv("PYTEST_CURRENT_TEST").split(" ")[0]
        self.test_file = self.full_name.split("::")[0].split("/")[-1].split(".py")[0]
        self.test_name = self.full_name.split("::")[1]
        self.test_scope = ""
        self.set_test_scope()

    def set_test_scope(self):
        self.test_scope = self.test_file


class DeviceConfig(object):
    def __init__(self, device_name, env_config):
        self.env_config = env_config
        self.build = self.env_config.build

        self.device_name = device_name.upper()

        self.desired_capabilities = getattr(DesiredCapabilities, f"{self.device_name}")

        self.platform_name = self.desired_capabilities["platformName"].lower()
        self.platform_version = self.desired_capabilities["platformVersion"]

        if "deviceGroup" in self.desired_capabilities:
            self.location = "kobiton"
        else:
            self.location = "local"

        self.run_location = {
            "local": "http://0.0.0.0:4723/wd/hub",
            "kobiton": "http://AlexKarpinski:b8cc7ed1-eba5-4b60-9ece-5bcd709d6dc2@api.kobiton.com/wd/hub",
        }[self.location]


class EnvConfig(object):
    def __init__(self, env, build):
        SUPPORTED_ENVS = ["dev", "prod", "staging"]

        self.env = env.lower()

        if self.env not in SUPPORTED_ENVS:
            raise Exception(
                f"{env} is not a supported environment (supported envs: {SUPPORTED_ENVS})"
            )

        self.build = build
