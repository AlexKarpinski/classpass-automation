from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class HomeLocators:
    def __init__(self, config):
        self.config = config

        self.WELCOME_LABEL = {
            "android": (By.ID, "com.classpass.classpass:id/bottom_nav_title"),
            "ios": (MobileBy.ACCESSIBILITY_ID, "For You"),
        }[self.config.platform_name]

        self.HOME_ICON_TAP_BAR = {
            "android": (By.XPATH, "//android.widget.FrameLayout[@content-desc='Home']"),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Home']"),
        }[self.config.platform_name]

        self.SEARCH_ICON_TAP_BAR = {
            "android": (By.XPATH, "//android.widget.FrameLayout[@content-desc='Search']"),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Search']"),
        }[self.config.platform_name]

        self.CLOSE_TRIAL_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[@text='Try ClassPass']/../*[1]"),
            "ios": (MobileBy.ACCESSIBILITY_ID, "cross"),
        }[self.config.platform_name]
