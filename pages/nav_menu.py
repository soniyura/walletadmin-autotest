from playwright.sync_api import Page

class NavMenu:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_application_info(self):
        self.page.get_by_test_id("application-info-link").click()