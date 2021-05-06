import allure
import pytest

from page_object.views.login_view import Login
from page_object.views.profile_view import Profile
from data.constants import Constants
from page_object.views.home_view import Home
from page_object.views.search_view import Search


class TestSearchViewImages:
    @pytest.fixture(scope="class")
    def search_view(self, driver, config, env_config):
        # Log in
        login = Login(driver=driver, config=config)
        login.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)
        if config.platform_name == "android" and config.platform_version == "7.0":
            login.deny_permissions()
        elif config.platform_name == "android" and config.platform_version == "10":
            login.deny_permissions_android_10()

        # Home
        home = Home(driver=driver, config=config)
        home.close_trial_button_click()
        home.open_search_screen()

        # Search
        search = Search(driver=driver, config=config)

        yield search

        profile = Profile(driver=driver, config=config)
        profile.log_out()

    @allure.title("Verify that user is able to open search screen, TC_SEARCH_001")
    def test_open_search_view(self, search_view, config):
        assert search_view.fitness_image_visibility()
        assert search_view.online_image_visibility()
        search_view.scroll_to_bottom(config)
        assert search_view.wellness_image_visibility()
        assert search_view.beauty_image_visibility()
        assert search_view.sports_and_recreation_image_visibility()
