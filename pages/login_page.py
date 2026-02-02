from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, base_url: str):
        self.page.goto(f"{base_url}/login")

    def login(self, username: str, password: str):
        self.page.get_by_test_id("username-input").fill(username)
        self.page.get_by_test_id("password-input").fill(password)
        self.page.get_by_test_id("sign-in-button").click()

    def download_config(self):
        self.page.get_by_role("button", name="Download").click()
