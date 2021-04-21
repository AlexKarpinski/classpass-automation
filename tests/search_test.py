import allure
import pytest

from page_object.views.searchClasses.search_class_view import SearchClass
from page_object.views.login_view import Login
from page_object.views.profile_view import Profile
from page_object.data.constants import Constants
from page_object.views.home_view import Home
from page_object.views.search_view import Search


class TestSearchView:

    @pytest.fixture(scope="class")
    def search_view(self, driver, config, env_config):
        # Log in
        login = Login(driver=driver, config=config)
        login.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)

        # Home
        home = Home(driver=driver, config=config)
        home.close_trial_button_click()
        home.open_search_screen()

        # Search
        search = Search(driver=driver, config=config)

        yield search

    @allure.title("Verify that user is able to open search screen, TC_SEARCH_001")
    def test_open_search_view(self, search_view, config):
        assert search_view.fitness_image_visibility()
        assert search_view.online_image_visibility()
        search_view.scroll_to_bottom(config)
        assert search_view.wellness_image_visibility()
        assert search_view.beauty_image_visibility()
        assert search_view.sports_and_recreation_image_visibility()

    @allure.title("Verify that user is able to open online category from search screen, TC_SEARCH_002")
    def test_open_online_view(self, search_view, driver, config):
        search_view.scroll_to_top()
        search_view.open_online()
        search_class = SearchClass(driver=driver, config=config)
        assert search_class.search_bar.has_text(Constants.ONLINE)


class TestSearchClassView:
    @pytest.fixture(scope="class")
    def search_class_view(self, driver, config):
        search_class = SearchClass(driver=driver, config=config)

        yield search_class

        if config.platform_name == "android":
            search_class.open_previous_screen()
        profile = Profile(driver=driver, config=config)
        profile.log_out()

    @allure.title("Filters bar: Verify that 'View by time', 'Time', 'Credits', 'Favorited', 'Amenities' pills are "
                  "available on filters bar, TC_SEARCH_003")
    def test_search_pills(self, search_class_view):
        assert search_class_view.filters_button_visibility()
        assert search_class_view.view_by_the_time_button_visibility()
        assert search_class_view.time_button_visibility()
        search_class_view.swipe_left_from_time_button()
        assert search_class_view.credits_button_visibility()
        assert search_class_view.amenities_button_visibility()

        search_class_view.open_previous_screen()

    @allure.title("Keyword Search - Verify that user is able to apply new activity on  allure_results screen, "
                  "TC_SEARCH_004")
    def test_search_activity(self, search_class_view):
        search_class_view.keyword_search_click()
        search_class_view.keyword_search_field.type(Constants.CYCLING)
        search_class_view.select_activity_from_results(Constants.CYCLING)
        assert search_class_view.search_bar.has_text(Constants.CYCLING)
