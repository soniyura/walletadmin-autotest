import re
from playwright.sync_api import Page, expect

class AssetsTableView:
    def __init__(self, page: Page): # создание конструктора класса
        self.page = page # инициализация страницы

    def _row_by_asset_name(self, asset_name: str):
        # Строка таблицы, в которой есть имя ассета (например "ULTIMA URC-20")
        return self.page.locator("tr", has=self.page.get_by_text(asset_name, exact=True)).first

    def assert_asset_switch_off(self, asset_name: str):
        row = self._row_by_asset_name(asset_name)
        expect(row).to_be_visible()

        # иногда строка может быть вне вьюпорта — скроллим к ней
        row.scroll_into_view_if_needed()

        # Внутри switch есть настоящий checkbox (MUI)
        checkbox = row.locator("input[type='checkbox']").first

        # input может быть "невидимым" (скрытый), поэтому проверяем что он в DOM
        expect(checkbox).to_be_attached()

        # главное: состояние выключено
        expect(checkbox).not_to_be_checked()