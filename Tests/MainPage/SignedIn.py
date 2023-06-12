from playwright.sync_api import sync_playwright, expect
from Pages.MainPage.MainPage import MainPage
from Requests.Analytics.GoogleAnalytics import GoogleAnalytics
from Requests.Analytics.Segment import Segment

main_page = MainPage()


def test_sign_in(username, password):
    page = main_page.sign_in(username, password)
    expect(page).to_have_url('https://www.chewy.com/app/account')
    expect(len(GoogleAnalytics.requests_list)).not_to_have_count(0)
    expect(len(Segment.requests_list)).not_to_have_count(0)
