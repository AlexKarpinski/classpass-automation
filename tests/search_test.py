import allure
import pytest
import json

from page_object.views.searchClasses.search_class_view import SearchClass
from page_object.views.login_view import Login
from page_object.views.profile_view import Profile
from page_object.data.constants import Constants
from page_object.views.home_view import Home
from page_object.views.search_view import Search

f = open('page_object/data/sourcesDataLondon.json', )
data = json.load(f)
classes = data['classes']
activities = data['activities']


class TestSearchViewImages:

    @pytest.fixture(scope="class")
    def search_view(self, driver, config, env_config):
        # Log in
        login = Login(driver=driver, config=config)
        login.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)
        if config.platform_name == 'android':
            login.deny_permissions()

        # Home
        home = Home(driver=driver, config=config)
        home.close_trial_button_click()
        home.open_search_screen()

        # Search
        search = Search(driver=driver, config=config)

        yield search

        search.scroll_to_top()
        home.open_home_screen()

    @allure.title("Verify that user is able to open search screen, TC_SEARCH_001")
    def test_open_search_view(self, search_view, config):
        assert search_view.fitness_image_visibility()
        assert search_view.online_image_visibility()
        search_view.scroll_to_bottom(config)
        assert search_view.wellness_image_visibility()
        assert search_view.beauty_image_visibility()
        assert search_view.sports_and_recreation_image_visibility()


class TestSearchClassView:
    @pytest.fixture(scope="function")
    def search_view(self, driver, config):
        home = Home(driver=driver, config=config)
        home.open_search_screen()

        search = Search(driver=driver, config=config)

        yield search

        search_class = SearchClass(driver=driver, config=config)
        search_class.open_previous_screen()

    @pytest.mark.parametrize("activity", activities.values())
    @allure.title("Keyword Search - Verify that user is able to apply new activity on result screen, TC_SEARCH_004")
    def test_search_activity(self, search_view, driver, config, activity):
        search_view.keyword_search_click()
        search_view.keyword_search_field.type(activity)
        search_view.select_activity_from_results(activity, config)
        search_class_view = SearchClass(driver=driver, config=config)
        assert search_class_view.search_bar.has_text(activity)
        assert search_class_view.source_by_name_visibility(data[activity]['name' + config.platform_name])

    @pytest.mark.parametrize("classes_type", classes.values())
    @allure.title("Verify that user is able to open category from search screen, TC_SEARCH_002")
    def test_open_categories(self, search_view, config, driver, classes_type):
        search_view.open_class_by_name(classes_type, config)
        search_class_view = SearchClass(driver=driver, config=config)
        assert search_class_view.search_bar.has_text(classes_type)
        assert search_class_view.source_by_name_visibility(data[classes_type]['name' + config.platform_name])


class TestSearchClassesFilters:
    @pytest.fixture(scope="class")
    def search_class_view(self, driver, config):
        home = Home(driver=driver, config=config)
        home.open_search_screen()

        search = Search(driver=driver, config=config)
        search.scroll_to_bottom(config)
        search.open_sports_and_recreation(config)

        search_class = SearchClass(driver=driver, config=config)

        yield search_class

        if config.platform_name == "android":
            search_class.open_previous_screen()

        profile = Profile(driver=driver, config=config)
        profile.log_out()

    @allure.title("Filters bar: Verify that 'View by time', 'Time', 'Credits', 'Favorited', 'Amenities' pills are "
                  "available on filters bar, TC_SEARCH_003")
    def test_filter_pills(self, search_class_view, config):
        assert search_class_view.filters_button_visibility()
        assert search_class_view.view_by_the_time_button_visibility()
        assert search_class_view.time_button_visibility()
        if config.platform_name == "android":
            search_class_view.swipe_left_from_time_button()
            assert search_class_view.credits_button_visibility()
            assert search_class_view.amenities_button_visibility()
