from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class SearchClassLocators:
    def __init__(self, config):
        self.config = config

        self.FILTERS_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[@text='Filters']/.."),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Filters']"),
        }[self.config.platform_name]

        self.VIEW_BY_THE_TIME_BUTTON = {
            "android": (By.XPATH, "//*[contains(@text, 'View by time')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'View by time'`]"),
        }[self.config.platform_name]

        self.TIME_BUTTON = {
            "android": (By.XPATH, "//*[contains(@text, 'Time')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Time'`]"),
        }[self.config.platform_name]

        self.CREDITS_BUTTON = {
            "android": (By.XPATH, "//*[contains(@text, 'Credits')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Credits'`]"),
        }[self.config.platform_name]

        self.FAVORITES_BUTTON = {
            "android": (By.XPATH, "//*[contains(@text, 'Favorites')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Favorited'`]"),
        }[self.config.platform_name]

        self.AMENITIES_BUTTON = {
            "android": (By.XPATH, "//*[contains(@text, 'Amenities')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Amenities'`]"),
        }[self.config.platform_name]

        self.SEARCH_BAR = {
            "android": (By.ID, "com.classpass.classpass:id/searchBarText"),
            "ios": (MobileBy.ACCESSIBILITY_ID, "keywordSearchBar"),
        }[self.config.platform_name]

        self.BACK_BUTTON = {
            "android": (By.ID, "com.classpass.classpass:id/exploreBackButton"),
            "ios": (MobileBy.ACCESSIBILITY_ID, "back-button"),
        }[self.config.platform_name]

        self.APPLY_BUTTON = {
            "android": (By.ID, ""),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Apply']"),
        }[self.config.platform_name]

        self.CANCEL_PERMISSIONS_BUTTON = {
            "android": (By.ID, "com.classpass.classpass:id/md_buttonDefaultNegative"),
            "ios": None,
        }[self.config.platform_name]
