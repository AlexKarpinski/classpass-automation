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

    def open_previous_screen(self):
        self.back_button.click()

    def login_into_app(self, email, password):
        self.login_button.click()
        self.email_field.input_without_hide_keyboard(email)
        self.password_field.type(password)
        self.log_in_button.click()
