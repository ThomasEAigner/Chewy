#Pages would be where each set of functions would be for navigation or complicated checks

from playwright.sync_api import sync_playwright
import Requests.Common as Common
from Pages.SignInPage.SignInPage import SignInPage

ChewyURL = 'https://www.chewy.com/'
#setting here for ease right now.  This should be set in a config file so that different browsers can be tested using the same code.
browser_type = 'firefox'


class MainPage:

    def navigate_to_main_page(self):
        print(ChewyURL)
        with sync_playwright() as p:
            if browser_type == 'firefox':
                browser = p.firefox.launch()
            if browser_type == 'chrome':
                browser = p.chromium.launch()
            page = browser.new_page()
            # This will pass all request events to the request_process method
            page.on("request", lambda request: Common.request_process(request))
            page.goto(ChewyURL)
        return page

    def sign_in(self, username, password):
        sign_in_page = SignInPage()
        page = self.navigate_to_main_page()
        sign_in_page.sign_in(page, username, password)
        return page





