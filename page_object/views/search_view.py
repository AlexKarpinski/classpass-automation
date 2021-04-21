from appium.webdriver.common.touch_action import TouchAction

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

    def scroll_to_bottom(self, config):
        if config.platform_name == "android":
            actions = TouchAction(self.driver)
            actions.press(x=500, y=2000).wait(1000).move_to(x=10, y=0).release().perform()
        elif config.platform_name == "ios":
            self.scroll_up_from(self.online_image)

    def scroll_to_top(self):
        self.scroll_down_from(self.wellness_image)

    def fitness_image_visibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for(locators.FITNESS_IMAGE)

    def online_image_visibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for(locators.ONLINE_IMAGE)

    def wellness_image_visibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for(locators.WELLNESS_IMAGE)

    def beauty_image_visibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for(locators.BEAUTY_IMAGE)

    def sports_and_recreation_image_visibility(self):
        locators = SearchLocators(config=self.config)
        return self.wait_for(locators.SPORTS_AND_RECREATION_IMAGE)

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

    def open_sports_and_recreation(self):
        self.sports_and_recreation_image.click()
