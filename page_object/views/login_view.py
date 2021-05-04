import allure

from page_object.locators.login_locators import LoginLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class Login(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = LoginLocators(config=self.config)

    def login_label_invisibility(self):
        locators = LoginLocators(config=self.config)
        with allure.step("THEN Login label should be invisible"):
            return self.wait_for_invisibility(locators.LOGIN_LABEL)

    @property
    def login_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.LOGIN_BUTTON)

    @property
    def email_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.EMAIL_FIELD)

    @property
    def password_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.PASSWORD_FIELD)

    @property
    def log_in_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.LOG_IN_BUTTON)

    @property
    def unsuccessful_login_message(self):
        return BaseElement(driver=self.driver, locator=self.locators.UNSUCCESSFUL_LOGIN_MESSAGE)

    @property
    def back_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.BACK_BUTTON)

    @property
    def deny_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.DENY_BUTTON)

    def deny_permissions(self):
        with allure.step("AND User clicks on deny button"):
            self.deny_button.click()

    @property
    def deny_button_android_10(self):
        return BaseElement(driver=self.driver, locator=self.locators.DENY_BUTTON_ANDROID_10)

    def deny_permissions_android_10(self):
        with allure.step("AND User clicks on deny button"):
            self.deny_button_android_10.click()

    def open_previous_screen(self):
        self.back_button.click()

    def login_into_app(self, email, password):
        with allure.step("WHEN User clicks on the login button"):
            self.login_button.click()
        with allure.step(f"AND User inputs {email} as email"):
            self.email_field.input(email)
        with allure.step(f"AND User inputs {password} as password"):
            self.password_field.input(password)
        with allure.step('AND User clicks on the login button'):
            self.log_in_button.click()
