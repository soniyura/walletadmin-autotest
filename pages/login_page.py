from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str, base_url: str):
        self.page.goto(f"{base_url}/login")
        self.page.get_by_test_id("username-input").fill(username)
        self.page.get_by_test_id("password-input").fill(password)
        self.page.get_by_test_id("sign-in-button").click()
        self.page.get_by_role("button", name="Download").click()


