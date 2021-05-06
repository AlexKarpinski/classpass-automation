from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class SearchLocators:
    def __init__(self, config):
        self.config = config

        self.FITNESS_IMAGE = {
            "android": (
                By.XPATH,
                "//android.widget.TextView[contains(@text, 'Fitness')]/..",
            ),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Fitness']"),
        }[self.config.platform_name]

        self.ONLINE_IMAGE = {
            "android": (
                By.XPATH,
                "//android.widget.TextView[contains(@text, 'Online')]/..",
            ),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Online']"),
        }[self.config.platform_name]

        self.WELLNESS_IMAGE = {
            "android": (
                By.XPATH,
                "//android.widget.TextView[contains(@text, 'Wellness')]/..",
            ),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Wellness']"),
        }[self.config.platform_name]

        self.BEAUTY_IMAGE = {
            "android": (
                By.XPATH,
                "//android.widget.TextView[contains(@text, 'Beauty')]/..",
            ),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='Beauty']"),
        }[self.config.platform_name]

        self.SPORTS_AND_RECREATION_IMAGE = {
            "android": (
                By.XPATH,
                "//android.widget.TextView[contains(@text, 'Sports and Recreation')]/..",
            ),
            "ios": (
                By.XPATH,
                "//XCUIElementTypeStaticText[@name='Sports and Recreation']",
            ),
        }[self.config.platform_name]

        self.KEYWORD_SEARCH = {
            "android": (
                By.XPATH,
                "//android.widget.TextView[@text='Find a venue or activity']",
            ),
            "ios": (MobileBy.ACCESSIBILITY_ID, "keywordSearchBar"),
        }[self.config.platform_name]

        self.KEYWORD_SEARCH_FIELD = {
            "android": (
                By.XPATH,
                "//android.widget.EditText[@text='Find an activity or venue']",
            ),
            "ios": (
                By.XPATH,
                "(//XCUIElementTypeOther[@name='Find an activity or venue'])[2]/XCUIElementTypeTextField",
            ),
        }[self.config.platform_name]

        self.BACK_BUTTON = {
            "android": (
                By.XPATH,
                "//android.widget.ImageButton[@content-desc='Navigate up']",
            ),
            "ios": (MobileBy.ACCESSIBILITY_ID, "Back"),
        }[self.config.platform_name]

        self.CANCEL_PERMISSIONS_BUTTON = {
            "android": (By.ID, "com.classpass.classpass:id/md_buttonDefaultNegative"),
            "ios": None,
        }[self.config.platform_name]
