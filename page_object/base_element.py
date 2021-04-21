import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.element = None
        self.find()

    def find(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(locator=self.locator)
            )
            self.element = element
            return None
        except TimeoutException:
            print(f"\nERROR: cannot find the element using a locator {self.locator}. ")
            return None

    def click(self):
        if self.element is not None:
            try:
                element = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(locator=self.locator)
                )
                element.click()
                return None
            except TimeoutException:
                print(
                    f"\nERROR: cannot click the element using a locator {self.locator}. "
                )
                return None
        else:
            return None

    @property
    def text(self):
        if self.element is not None:
            try:
                text = self.element.text
                return text
            except AttributeError:
                print(
                    "\nERROR: the element doesn't have attribute text.\n",
                    sys.exc_info()[:2],
                )
                return None
        else:
            return None

    @property
    def upper_text(self):
        try:
            text = self.element.text
            return text.upper()
        except AttributeError:
            print("Error: the element doesn't have attribute text: ", sys.exc_info()[0])
            return None

    def has_text(self, value):
        if self.element is not None:
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.text_to_be_present_in_element(locator=self.locator, text_=value)
                )
                return True
            except TimeoutException:
                print(
                    f"\nFailed: the text {value} isn't present in the element using the locator {self.locator}.\n",
                    sys.exc_info()[:2],
                )
                return False
        else:
            return None

    def input_without_hide_keyboard(self, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator=self.locator)
            )
            element.clear()
            element.set_value(text)
        except TimeoutException:
            print("ERROR: cannot click the element: ", sys.exc_info()[0])
            return None

    def input(self, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator=self.locator)
            )
            element.clear()
            element.set_value(text)
            self.driver.hide_keyboard()
        except TimeoutException:
            print("ERROR: cannot click the element: ", sys.exc_info()[0])
            return None

    def set_value(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.clear()
        element.set_value(text)

    def clear(self):
        self.element.clear()

    @property
    def location(self):
        location = self.element.location
        return location

    @property
    def visible(self):
        if self.element is not None:
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of(self.element))
                return True
            except TimeoutException:
                print(
                    "Error: element not visible after 10 seconds: ", sys.exc_info()[0]
                )
                return False
            except Exception as e:
                print(f"An Exception occurred: {e}")
                return False
        else:
            return False

    def type(self, text):
        try:
            self.element.send_keys(text)
            return None
        except Exception as e:
            print(f"An Exception occurred: {e}")
            return None

    @property
    def elements_list(self):
        try:
            elements = self.driver.find_elements(self.locator)
            return elements
        except TimeoutException:
            print("Error: cannot find the elements: ", sys.exc_info()[0])
            return None
