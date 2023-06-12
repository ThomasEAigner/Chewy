#Tests would be where the actual test can be found.  You can run everything in a folder or just a single file.

from playwright.sync_api import sync_playwright, expect
from Pages.MainPage.MainPage import MainPage
from Requests.Analytics.GoogleAnalytics import GoogleAnalytics

main_page = MainPage()


def test_collect_all_analytics_on_page_load():
    main_page.navigate_to_main_page('firefox')
    expect(len(GoogleAnalytics.requests_list)).not_to_have_count(0)


def test_click_brands():
    print("Test for when brands is clicked while not signed in")