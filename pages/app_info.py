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





# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto("https://walletadmin.plcu.team/login")
#     page.get_by_test_id("username-input").click()
#     page.get_by_test_id("username-input").fill("yurii.katerynenko")
#     page.get_by_test_id("password-input").click()
#     page.get_by_test_id("password-input").fill("mRYXv53W1ZXG")
#     page.get_by_test_id("sign-in-button").click()
#     page.get_by_role("button", name="Download").click()
#
#     page.get_by_test_id("application-info-link").click()
#
#     page.locator("form").filter(has_text="AndroidApplication").get_by_role("button").click()
#     page.get_by_role("textbox", name="Current Version Code").click()
#     page.get_by_role("textbox", name="Current Version Code").click()
#     page.get_by_role("textbox", name="Current Version Code").click()
#     page.get_by_role("textbox", name="Current Version Code").fill("4858")
#     page.get_by_role("textbox", name="Current Version Name").click()
#     page.get_by_role("textbox", name="Current Version Name").click()
#     page.get_by_role("textbox", name="Current Version Name").click()
#     page.get_by_role("textbox", name="Current Version Name").fill("1.26.1")
#     page.get_by_role("textbox", name="MIN Version Code").click()
#     page.get_by_role("textbox", name="MIN Version Code").fill("4857")
#     page.get_by_role("textbox", name="MIN Version Name").click()
#     page.get_by_role("textbox", name="MIN Version Name").click()
#     page.get_by_role("textbox", name="MIN Version Name").fill("1.26.1")
#     page.get_by_role("button", name="Confirm").click()
#     page.get_by_text("4858").click()
#     page.get_by_text("1.26.1").first.click()
#     page.get_by_text("4857").click()
#     page.get_by_text("1.26.1").nth(1).click()
#     page.get_by_test_id("confirm-button").click()
#     page.get_by_text("You have unpublished changes").dblclick()
#     page.get_by_text("You have unpublished changes").click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
