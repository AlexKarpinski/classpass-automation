import allure
import pytest

from pytest import mark
from page_object.views.home_view import Home
from page_object.views.login_view import Login
from page_object.views.profile_view import Profile
from data.constants import Constants


class TestLoginView:
    @pytest.fixture(scope="class")
    def login_view(self, driver, config, env_config):
        # Log in
        login = Login(driver=driver, config=config)

        yield login

        profile = Profile(driver=driver, config=config)
        profile.log_out()

    @pytest.fixture(scope="function")
    def open_previous_screen(self, driver, config):
        yield
        login = Login(driver=driver, config=config)
        with allure.step("WHEN User opens previous screen"):
            login.open_previous_screen()

    @mark.smoke
    @allure.title(
        "Verify that user can't login to the app with non-existing email, TC_LOGIN_002"
    )
    def test_login_negative(self, login_view, open_previous_screen):
        login_view.login_into_app(Constants.USER_NAME, Constants.INVALID_PASSWORD)
        message_text = login_view.unsuccessful_login_message.text
        with allure.step("THEN Message should appeared"):
            assert message_text == Constants.UNSUCCESSFUL_LOGIN_MESSAGE_TEXT

    @mark.smoke
    @allure.title(
        "Verify that user can log in to the app with valid email and password, TC_LOGIN_001"
    )
    def test_login_positive(self, driver, config, login_view):
        login_view.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)
        if config.platform_name == "android" and config.platform_version == "7.0":
            login_view.deny_permissions()
        elif config.platform_name == "android" and config.platform_version == "10":
            login_view.deny_permissions_android_10()
        assert login_view.login_label_invisibility()
        home = Home(driver=driver, config=config)
        home.close_trial_button_click()
        with allure.step(f"THEN for you label should be visible"):
            assert home.welcome_label.visible
