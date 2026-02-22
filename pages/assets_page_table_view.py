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









    def assert_network_dropdown_default_all(self):
        expect(
            self.page.get_by_role("combobox")
        ).to_have_text("ALL NETWORKS")


    def open_networks_dropdown(self):
        self.page.get_by_role("combobox").click()

    def select_network(self, network_name: str):
        self.open_networks_dropdown()
        self.page.get_by_role("listbox") \
            .get_by_role("option", name=network_name) \
            .click()

    def click_network_option(self, network_name: str):
        self.page.get_by_role("listbox") \
            .get_by_role("option", name=network_name) \
            .click()


    def assert_table_has_ticker(self, ticker: str):
        # проверяем только колонку Ticker (3-я колонка)
        cells = self.page.locator("tbody tr td:nth-child(3)", has_text=ticker)

        # если есть хотя бы одна такая ячейка — ок
        expect(cells.first).to_be_visible()
        assert cells.count() > 0, f"Ticker '{ticker}' not found in Ticker column"
