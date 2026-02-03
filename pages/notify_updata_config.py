import re
from playwright.sync_api import Page, expect


class Notify_updata_config():
    def __init__(self, page: Page):
        self.page = page

    def banner_unpublished_changes(self):
        expect(self.page.get_by_text(
            re.compile(r"You have unpublished changes in .* config file\.?")
        )).to_be_visible()

        publish_button = self.page.get_by_role("button", name="Publish")
        expect(publish_button).to_be_visible()
        expect(publish_button).to_be_enabled()