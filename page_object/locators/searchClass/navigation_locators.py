from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class NavigationLocators:
    def __init__(self, config):
        self.config = config

        self.EXPLORE_BUTTON = {
            "android": (By.ID, "//android.widget.CheckedTextView[@content-desc='Explore']"),
            "ios": (By.XPATH, ""),
        }[self.config.platform_name]
