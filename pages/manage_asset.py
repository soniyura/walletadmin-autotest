import re
from playwright.sync_api import Page, expect

class ManageAssetPage:
    def __init__(self, page: Page):
        self.page = page

    def assert_opened_manage_asset_page(self):
        expect(self.page.get_by_text("Manage Asset", exact=True)).to_be_visible()

    def assert_default_state_switch_off(self):
        label = self.page.get_by_text("Default State", exact=True).first
        expect(label).to_be_visible()

        # ВАЖНО: прокрутить к элементу (на случай ленивой отрисовки)
        label.scroll_into_view_if_needed()

        # Ищем ближайший контейнер, в котором есть checkbox
        # (этот XPath поднимется вверх до первого предка, содержащего input[type=checkbox])
        row = label.locator("xpath=ancestor::*[.//input[@type='checkbox']][1]")

        checkbox = row.locator("input[type='checkbox']").first
        expect(checkbox).to_be_attached()   # в DOM
        # visible может быть false, если input скрытый (у MUI так бывает)
        # поэтому лучше проверять именно состояние:
        expect(checkbox).not_to_be_checked()


    def cancel_btn_click(self):
        self.page.get_by_role("link", name="Cancel").click()