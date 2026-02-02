import re
from playwright.sync_api import Page, expect

class AssetsPage:
    def __init__(self, page: Page):
        self.page = page

    def assert_opened(self):
        expect(self.page).to_have_url(re.compile(r".*/assets/?(\?.*)?$"))
        expect(self.page.get_by_text("Assets", exact=True)).to_be_visible()

    def assert_network_filters_visible(self):
        # Если фильтры лежат в listbox/menu — ограничиваем область
        # Подстрой контейнер при необходимости:
        filters = self.page.locator("form")

        networks = ["SMARTCHAIN", "ULTIMA", "UCHAIN", "SMART", "TRON", "ETHEREUM", "BITCOIN"]
        for n in networks:
            loc = filters.get_by_text(n, exact=True)
            expect(loc.first).to_be_visible()

    def assert_not_empty(self):
        switches = self.page.locator('[role="switch"], input[type="checkbox"]')
        expect(switches.first).to_be_visible()
        assert switches.count() > 0

    def select_network_from_dropdown(self, network_ui_name: str):
        # по твоему скрину option/combobox — это прям то, что надо
        self.page.get_by_role("combobox").click()
        self.page.get_by_role("option", name=network_ui_name).click()
