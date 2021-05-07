import allure
import pytest
import json

from page_object.views.login_view import Login
from page_object.views.profile_view import Profile
from data.constants import Constants
from page_object.views.home_view import Home
from page_object.views.searchClasses.search_class_view import SearchClass
from page_object.views.search_view import Search

f = open(
    "data/sourcesDataLondon.json",
)
data = json.load(f)
sources = data["classes"]
activities = data["activities"]


class TestSearchSourcesView:
    @pytest.fixture(scope="class")
    def login(self, driver, config):
        # Log in
        login = Login(driver=driver, config=config)
        login.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)
        if config.platform_name == "android" and config.platform_version == "7.0":
            login.deny_permissions()
        elif config.platform_name == "android" and config.platform_version == "10":
            login.deny_permissions_android_10()
        home = Home(driver=driver, config=config)
        home.close_trial_button_click()

        yield

        profile = Profile(driver=driver, config=config)
        profile.log_out()

    @pytest.fixture(scope="function")
    def search_view(self, driver, config):
        home = Home(driver=driver, config=config)
        home.open_search_screen()

        search = Search(driver=driver, config=config)

        yield search

        search_class = SearchClass(driver=driver, config=config)
        search_class.open_previous_screen()
        home.open_home_screen()

    @pytest.mark.parametrize("activity", activities.values())
    @allure.title(
        "Keyword Search - Verify that user is able to apply new activity on result screen, TC_SEARCH_004"
    )
    def test_search_activity(self, login, search_view, driver, config, activity):
        search_view.keyword_search_click()
        search_view.keyword_search_field_type(activity)
        search_view.select_activity_from_results(activity, config)
        search_class_view = SearchClass(driver=driver, config=config)
        with allure.step(f"THEN Search bar should have text {activity}"):
            assert search_class_view.search_bar.has_text(activity)
        with allure.step(
                f"AND Source {data[activity]['name' + config.platform_name]} should be visible"
        ):
            assert search_class_view.source_by_name_visibility(
                data[activity]["name" + config.platform_name]
            )

    @pytest.mark.parametrize("sources_type", sources.values())
    @allure.title(
        "Verify that user is able to open category from search screen, TC_SEARCH_002"
    )
    def test_open_categories(self, search_view, config, driver, sources_type):
        search_view.open_category_by_name(sources_type, config)
        search_class_view = SearchClass(driver=driver, config=config)
        with allure.step(f"THEN Search bar should have text {sources_type}"):
            assert search_class_view.search_bar.has_text(sources_type)
        with allure.step(
                f"AND Source {data[sources_type]['name' + config.platform_name]} should be visible"
        ):
            assert search_class_view.source_by_name_visibility(
                data[sources_type]["name" + config.platform_name]
            )
