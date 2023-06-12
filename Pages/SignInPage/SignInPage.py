from playwright.sync_api import sync_playwright


class SignInPage:

    @staticmethod
    def sign_in(self, page, username, password):
        page.get_by_label("Email Address").fill("username")
        page.get_by_label("Password").fill("password")
        page.get_by_role("button", name="Sign In").click()