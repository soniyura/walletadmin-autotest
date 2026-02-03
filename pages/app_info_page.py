from playwright.sync_api import Page, expect

class AndroidBlock:
    def __init__(self, page: Page):
        self.page = page

    def update_version_info(self, current_version_code: str, current_version_name: str,
                            min_version_code: str, min_version_name: str):
        self.page.locator("form").filter(has_text="AndroidApplication").get_by_role("button").click()

        self.page.get_by_role("textbox", name="Current Version Code").fill(current_version_code)
        self.page.get_by_role("textbox", name="Current Version Name").fill(current_version_name)
        self.page.get_by_role("textbox", name="MIN Version Code").fill(min_version_code)
        self.page.get_by_role("textbox", name="MIN Version Name").fill(min_version_name)

        self.page.get_by_role("button", name="Confirm").click()

        expect(self.page.get_by_text(current_version_code)).to_be_visible()
        expect(self.page.get_by_text(current_version_name).first).to_be_visible()
        expect(self.page.get_by_text(min_version_code)).to_be_visible()
        expect(self.page.get_by_text(min_version_name).nth(1)).to_be_visible()

        self.page.get_by_role("button", name="Confirm").click()


class IosBlock:
    def __init__(self, page: Page):
        self.page = page

    def update_version_info(self, current_version_name: str, min_version_name: str):
        self.page.locator("form").filter(has_text="IosApplication").get_by_role("button").click()

        self.page.get_by_role("textbox", name="Current Version Name").fill(current_version_name)
        self.page.get_by_role("textbox", name="MIN Version Name").fill(min_version_name)

        self.page.get_by_role("button", name="Confirm").click()

        expect(self.page.get_by_text(current_version_name).first).to_be_visible()
        expect(self.page.get_by_text(min_version_name).nth(1)).to_be_visible()

        self.page.get_by_role("button", name="Confirm").click()


