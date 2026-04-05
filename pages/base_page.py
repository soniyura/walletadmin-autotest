import re
from playwright.sync_api import Page, expect
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Check that the banner is displayed - You have unpublished changes... ")
    def banner_unpublished_changes(self):
        expect(self.page.get_by_text(
            re.compile(r"You have unpublished changes in .* config file\.?")
        )).to_be_visible()

        publish_button = self.page.get_by_role("button", name="Publish")
        expect(publish_button).to_be_visible()
        expect(publish_button).to_be_enabled()

    @allure.step("Go to the Application Info page")
    def navigate_to_application_info(self):
        self.page.get_by_test_id("application-info-link").click()




