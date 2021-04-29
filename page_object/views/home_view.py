import allure

from selenium.common.exceptions import TimeoutException
from page_object.locators.home_locators import HomeLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class Home(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = HomeLocators(config=self.config)

    @property
    def welcome_label(self):
        self.wait_for(self.locators.WELCOME_LABEL, 10)
        return BaseElement(driver=self.driver, locator=self.locators.WELCOME_LABEL)

    @property
    def search_icon_tap_bar(self):
        self.wait_for(self.locators.WELCOME_LABEL, 10)
        return BaseElement(driver=self.driver, locator=self.locators.SEARCH_ICON_TAP_BAR)

    @property
    def close_trial_button(self):
        self.wait_for(self.locators.CLOSE_TRIAL_BUTTON, 10)
        return BaseElement(driver=self.driver, locator=self.locators.CLOSE_TRIAL_BUTTON)

    @property
    def home_icon_tap_bar(self):
        self.wait_for(self.locators.HOME_ICON_TAP_BAR, 20)
        return BaseElement(driver=self.driver, locator=self.locators.HOME_ICON_TAP_BAR)

    def open_search_screen(self):
        with allure.step("WHEN User opens search screen"):
            self.search_icon_tap_bar.click()

    def open_home_screen(self):
        with allure.step("WHEN User opens home screen"):
            self.home_icon_tap_bar.click()

    def close_trial_button_click(self):
        with allure.step("WHEN User closes trial view"):
            try:
                self.close_trial_button.click()
                return None
            except TimeoutException:
                print(f"\nERROR: cannot find the element using a locator {self.locator}. ")
                return None
