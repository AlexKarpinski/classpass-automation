import allure

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from page_object.locators.search_locators import SearchLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class Search(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = SearchLocators(config=self.config)

    @property
    def fitness_image(self):
        return BaseElement(driver=self.driver, locator=self.locators.FITNESS_IMAGE)

    @property
    def online_image(self):
        return BaseElement(driver=self.driver, locator=self.locators.ONLINE_IMAGE)

    @property
    def wellness_image(self):
        return BaseElement(driver=self.driver, locator=self.locators.WELLNESS_IMAGE)

    @property
    def beauty_image(self):
        return BaseElement(driver=self.driver, locator=self.locators.BEAUTY_IMAGE)

    @property
    def sports_and_recreation_image(self):
        return BaseElement(driver=self.driver, locator=self.locators.SPORTS_AND_RECREATION_IMAGE)

    @property
    def keyword_search(self):
        return BaseElement(driver=self.driver, locator=self.locators.KEYWORD_SEARCH)

    @property
    def back_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.BACK_BUTTON)

    @property
    def keyword_search_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.KEYWORD_SEARCH_FIELD)

    @property
    def cancel_permissions_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CANCEL_PERMISSIONS_BUTTON)

    def cancel_permissions(self):
        self.cancel_permissions_button.click()

    def scroll_to_bottom(self, config):
        with allure.step("WHEN User scrolls to bottom"):
            if config.platform_name == "android":
                actions = TouchAction(self.driver)
                actions.press(x=500, y=1850).wait(1000).move_to(x=500, y=0).release().perform()
            elif config.platform_name == "ios":
                self.scroll_up_from(self.online_image)

    def scroll_to_top(self):
        with allure.step("WHEN User scrolls to top"):
            self.scroll_down_from(self.wellness_image)

    def fitness_image_visibility(self):
        locators = SearchLocators(config=self.config)
        with allure.step("THEN fitness image should be visible"):
            return self.wait_for(locators.FITNESS_IMAGE)

    def online_image_visibility(self):
        locators = SearchLocators(config=self.config)
        with allure.step("AND online image should be visible"):
            return self.wait_for(locators.ONLINE_IMAGE)

    def wellness_image_visibility(self):
        locators = SearchLocators(config=self.config)
        with allure.step("THEN wellness image should be visible"):
            return self.wait_for(locators.WELLNESS_IMAGE)

    def beauty_image_visibility(self):
        locators = SearchLocators(config=self.config)
        with allure.step("AND beauty image should be visible"):
            return self.wait_for(locators.BEAUTY_IMAGE)

    def sports_and_recreation_image_visibility(self):
        locators = SearchLocators(config=self.config)
        with allure.step("AND sports and recreation image should be visible"):
            return self.wait_for(locators.SPORTS_AND_RECREATION_IMAGE)

    def image_visibility_by_name(self, name, config):
        if name == 'Wellness' or name == 'Beauty' or name == 'Sports and Recreation':
            self.scroll_to_bottom(config)
        IMAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text,'" + name + "')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='" + name + "']"),
        }[self.config.platform_name]
        return self.wait_for(IMAGE)

    def fitness_image_invisibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for_invisibility(locators.FITNESS_IMAGE)

    def online_image_invisibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for_invisibility(locators.ONLINE_IMAGE)

    def sports_and_recreation_image_invisibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for_invisibility(locators.SPORTS_AND_RECREATION_IMAGE)

    def open_fitness(self):
        self.fitness_image.click()

    def open_online(self):
        self.online_image.click()

    def open_category_by_name(self, name, config):
        if name == 'Wellness' or name == 'Beauty' or name == 'Sports and Recreation':
            self.scroll_to_bottom(config)
        IMAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text,'" + name + "')]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeStaticText[@name='" + name + "']"),
        }[self.config.platform_name]
        with allure.step(f"WHEN User clicks on the {name} image"):
            self.try_click(IMAGE)
        if config.platform_name == 'android':
            with allure.step("AND User clicks on the cancel button"):
                self.cancel_permissions()

    def open_sports_and_recreation(self, config):
        with allure.step("WHEN User opens sports and recreation category"):
            self.sports_and_recreation_image.click()
        if config.platform_name == 'android':
            with allure.step("AND User clicks in the cancel button"):
                self.cancel_permissions()

    def select_activity_from_results(self, activity, config):
        ACTIVITY_LOCATOR = {
            "android": (By.XPATH, "//android.widget.TextView[@text='" + activity + "']"),
            "ios": (By.XPATH, "(//XCUIElementTypeOther[@name='" + activity + "'])[4]"),
        }[self.config.platform_name]
        self.try_click(ACTIVITY_LOCATOR)
        if config.platform_name == 'android':
            self.cancel_permissions()

    def keyword_search_click(self):
        with allure.step("WHEN User clicks on the keyword search"):
            self.keyword_search.click()

    def keyword_search_field_type(self, activity):
        with allure.step(f"AND User types {activity} on the keyword search"):
            self.keyword_search_field.type(activity)

    def open_previous_screen(self):
        self.back_button.click()
