from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page_object.locators.searchClass.search_class_locators import SearchClassLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class SearchClass(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = SearchClassLocators(config=self.config)

    @property
    def filters_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.FILTERS_BUTTON)

    @property
    def view_by_the_time_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.VIEW_BY_THE_TIME_BUTTON)

    @property
    def time_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.TIME_BUTTON)

    @property
    def credits_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CREDITS_BUTTON)

    @property
    def favorites_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.FAVORITES_BUTTON)

    @property
    def amenities_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.AMENITIES_BUTTON)

    @property
    def search_bar(self):
        return BaseElement(driver=self.driver, locator=self.locators.SEARCH_BAR)

    @property
    def back_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.BACK_BUTTON)

    @property
    def apply_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.APPLY_BUTTON)

    @property
    def cancel_permissions_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CANCEL_PERMISSIONS_BUTTON)

    def cancel_permissions(self):
        self.cancel_permissions_button.click()

    def open_previous_screen(self):
        self.back_button.click()

    def filters_button_visibility(self):
        locators = SearchClassLocators(config=self.config)
        return self.wait_for(locators.FILTERS_BUTTON)

    def view_by_the_time_button_visibility(self):
        locators = SearchClassLocators(config=self.config)
        return self.wait_for(locators.VIEW_BY_THE_TIME_BUTTON)

    def time_button_visibility(self):
        locators = SearchClassLocators(config=self.config)
        return self.wait_for(locators.TIME_BUTTON)

    def credits_button_visibility(self):
        locators = SearchClassLocators(config=self.config)
        return self.wait_for(locators.CREDITS_BUTTON)

    def favorites_button_visibility(self):
        locators = SearchClassLocators(config=self.config)
        return self.wait_for(locators.FAVORITES_BUTTON)

    def amenities_button_visibility(self):
        locators = SearchClassLocators(config=self.config)
        return self.wait_for(locators.AMENITIES_BUTTON)

    def swipe_left_from_time_button(self):
        self.swipe_left_from(self.time_button)

    def select_activity_from_results(self, activity, config):
        ACTIVITY_LOCATOR = {
            "android": (By.XPATH, "//android.widget.TextView[@text='" + activity + "']"),
            "ios": (By.XPATH, "(//XCUIElementTypeOther[@name='" + activity + "'])[4]"),
        }[self.config.platform_name]
        self.try_click(ACTIVITY_LOCATOR)
        if config.platform_name == 'android':
            self.cancel_permissions()

    def keyword_search_click(self):
        self.search_bar.click()

    def source_by_name_visibility(self, name):
        SOURCE = {
            "android": (By.XPATH, '//*[@text="' + name + '"]'),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='" + name + "']"),
        }[self.config.platform_name]
        return self.wait_for(SOURCE)
