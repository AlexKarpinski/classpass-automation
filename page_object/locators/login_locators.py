from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class LoginLocators:
    def __init__(self, config):
        self.config = config

        self.LOGIN_LABEL = {
            "android": (
                By.XPATH,
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                ".ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                ".TextView",
            ),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Log in with account']"),
        }[self.config.platform_name]

        self.LOGIN_BUTTON = {
            "android": (MobileBy.ACCESSIBILITY_ID, "Log in with account"),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Log in with account']"),
        }[self.config.platform_name]

        self.EMAIL_FIELD = {
            "android": (
                By.XPATH,
                "//android.widget.EditText[contains(@text, 'Email address')]",
            ),
            "ios": (
                By.XPATH,
                "(//XCUIElementTypeOther[@name='Email address'])[2]/XCUIElementTypeTextField",
            ),
        }[self.config.platform_name]

        self.PASSWORD_FIELD = {
            "android": (
                By.XPATH,
                "//android.widget.EditText[contains(@text, 'Password')]",
            ),
            "ios": (
                By.XPATH,
                "(//XCUIElementTypeOther[@name='Password'])[2]/XCUIElementTypeSecureTextField",
            ),
        }[self.config.platform_name]

        self.LOG_IN_BUTTON = {
            "android": (
                By.XPATH,
                "(//android.widget.TextView[contains(@text, 'Log in')])[2]/..",
            ),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Log in']"),
        }[self.config.platform_name]

        self.UNSUCCESSFUL_LOGIN_MESSAGE = {
            "android": (
                By.XPATH,
                "//android.widget.TextView[contains(@text, 'The password or email')]",
            ),
            "ios": (
                MobileBy.NAME,
                "The password or email address you entered is incorrect. Reset your password or "
                "contact us if youʼre having trouble logging in.",
            ),
        }[self.config.platform_name]

        self.BACK_BUTTON = {
            "android": (
                By.XPATH,
                "//android.widget.ImageButton[@content-desc='Navigate up']",
            ),
            "ios": (MobileBy.ACCESSIBILITY_ID, "Back"),
        }[self.config.platform_name]

        self.DENY_BUTTON = {
            "android": (
                By.ID,
                "com.android.packageinstaller:id/permission_deny_button",
            ),
            "ios": None,
        }[self.config.platform_name]

        self.DENY_BUTTON_ANDROID_10 = {
            "android": (
                By.ID,
                "com.android.permissioncontroller:id/permission_deny_button",
            ),
            "ios": None,
        }[self.config.platform_name]
