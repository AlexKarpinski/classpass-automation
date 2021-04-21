from appium.webdriver.common.touch_action import TouchAction

from page_object.locators.searchClass.navigation_locators import NavigationLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class Navigation(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = NavigationLocators(config=self.config)

    @property
    def explore_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.EXPLORE_BUTTON)

    def swipe_left(self):
        window_size = self.driver.get_window_size()
        width = window_size["width"] / 2
        height = window_size["height"] / 2
        actions = TouchAction(self.driver)
        actions.press(x=width, y=height).wait(1000).move_to(x=0, y=height).release().perform()


