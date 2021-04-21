from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class SearchLocators:
    def __init__(self, config):
        self.config = config

        self.FITNESS_IMAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Fitness')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Fitness']"),
        }[self.config.platform_name]

        self.ONLINE_IMAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Online')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Online']"),
        }[self.config.platform_name]

        self.WELLNESS_IMAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Wellness')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Wellness']"),
        }[self.config.platform_name]

        self.BEAUTY_IMAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Beauty')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Beauty']"),
        }[self.config.platform_name]

        self.SPORTS_AND_RECREATION_IMAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Sports and Recreation')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Sports and Recreation']"),
        }[self.config.platform_name]
