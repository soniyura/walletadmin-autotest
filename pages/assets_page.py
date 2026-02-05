from playwright.sync_api import Page, expect
from pages.assets_page_section_view import AssetsSectionView
from pages.assets_page_table_view import AssetsTableView
from pages.assets_page_sorting_mode import AssetsSortingMode


class AssetsPage:
    def __init__(self, page: Page):
        self.page = page

    # общие кнопки режимов
    def open_table_view(self):
        self.page.get_by_role("button", name="Table View").click()
        view = AssetsTableView(self.page)
        view.assert_opened()
        return view

    def open_section_view(self):
        self.page.get_by_role("button", name="Section View").click()
        view = AssetsSectionView(self.page)
        view.assert_opened()
        return view

    def open_sorting_mode(self):
        self.page.get_by_role("button", name="Sorting Mode").click()
        view = AssetsSortingMode(self.page)
        view.assert_opened()
        return view

    # # общие проверки страницы
    # def assert_opened(self):
    #     expect(self.page.get_by_text("Assets", exact=True)).to_be_visible()
