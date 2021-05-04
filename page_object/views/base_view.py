import sys

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException
)


class BaseView(object):
    def __init__(self, driver, config):
        self.locator = None
        self.driver = driver
        self.config = config

    def wait_for(self, locator, wait_time=20):

        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )

        except TimeoutException:
            print("Error: cannot find the element: ", sys.exc_info()[0])
            return None

    def try_click(self, locator, wait_time=10):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            ).click()

        except TimeoutException:
            print("Error: cannot click the element: ", sys.exc_info()[0])
            return None

    def wait_for_invisibility(self, locator, wait_time=15):
        # print("Explicitly waiting for element to be invisible '{0}' for '{1}' seconds ".format(locator, wait_time))
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.invisibility_of_element_located(locator)
            )

        except TimeoutException:
            print("Error: element is visible: ", sys.exc_info()[0])
            return None

    def wait_for_clickability(self, locator, wait_time=15):
        # print("Explicitly waiting for element to be invisible '{0}' for '{1}' seconds ".format(locator, wait_time))
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )

        except TimeoutException:
            print("Error: element is visible: ", sys.exc_info()[0])
            return None

    def scroll_up_from(self, origin_element):
        try:
            origin_el = origin_element.element
        except AttributeError:
            origin_el = origin_element
        actions = TouchAction(self.driver)
        actions.press(origin_el).wait(1000).move_to(
            x=10, y=0
        ).release().perform()

    # Swipe down from any element
    def scroll_down_from(self, origin_element):
        try:
            origin_el = origin_element.element
        except AttributeError:
            origin_el = origin_element
        actions = TouchAction(self.driver)
        actions.press(origin_el).wait(1000).move_to(x=10, y=2500).release().perform()

    # Swipe left from any element
    def swipe_left_from(self, origin_element):
        try:
            origin_el = origin_element.element
        except AttributeError:
            origin_el = origin_element
        actions = TouchAction(self.driver)
        actions.press(origin_el).wait(1000).move_to(x=-1000, y=10).release().perform()

    # Swipe right from any element
    def swipe_right_from(self, origin_element):
        try:
            origin_el = origin_element.element
        except AttributeError:
            origin_el = origin_element
        actions = TouchAction(self.driver)
        actions.press(origin_el).wait(1000).move_to(x=2000, y=10).release().perform()

    def swipe_from_to(self, origin_element, destination_element):
        try:
            origin_el = origin_element.element
            destination_el = destination_element.element
        except AttributeError:
            origin_el = origin_element
            destination_el = destination_element
        actions = TouchAction(self.driver)
        actions.press(origin_el).wait(1000).move_to(destination_el).release().perform()

    def scroll(self, origin_element, destination_element, duration=600):
        origin_el = origin_element.element
        destination_el = destination_element.element
        action = TouchAction(self.driver)
        if duration is None:
            action.press(origin_el).move_to(destination_el).release().perform()
        else:
            action.press(origin_el).wait(duration).move_to(
                destination_el
            ).release().perform()
        return self
