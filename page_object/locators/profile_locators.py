from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class ProfileLocators:
    def __init__(self, config):
        self.config = config

        self.SETTINGS_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Settings')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Settings']"),
        }[self.config.platform_name]

        self.LOG_OUT_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Log out')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeOther[@name='Log out']"),
        }[self.config.platform_name]

        self.PROFILE_ICON = {
            "android": (By.ID, "com.classpass.classpass:id/profile_tab"),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Profile']"),
        }[self.config.platform_name]

        self.SUPPORT_LABEL = {
            "android": (By.ID, "com.classpass.classpass.dev:id/profile_tab"),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Support']"),
        }[self.config.platform_name]
