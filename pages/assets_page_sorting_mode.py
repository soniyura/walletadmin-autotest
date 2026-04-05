import re
from playwright.sync_api import Page, expect
import allure

class AssetsSortingMode:
    def __init__(self, page: Page): # создание конструктора класса
        self.page = page # инициализация страницы

    """
    Методы для взаимодействия с режимом сортировки ассетов. C209626
    """
    def _rows(self):
        return self.page.locator("tbody tr")

    def _drag_handle_in_row(self, row):
        """
        Для react-beautiful-dnd хэндл обычно имеет data-rfd-drag-handle-draggable-id.
        Если его нет — делаем запасной вариант (первая "кнопка" / cell в начале строки).
        """
        handle = row.locator("[data-rfd-drag-handle-draggable-id]").first
        if handle.count() > 0:
            return handle

        # fallback 1: часто handle — это td с role=button (по твоему скрину)
        role_btn = row.get_by_role("button").first
        if role_btn.count() > 0:
            return role_btn

        # fallback 2: самый первый td (как крайний вариант)
        return row.locator("td").first

    # метод для перетаскивания строки вниз на определенное количество позиций
    @allure.step("dragging a row down by a certain number of positions")
    def drag_row_down(self, source_text: str, positions: int = 1):
        assert positions > 0

        rows = self._rows()
        expect(rows.first).to_be_visible()

        # ищем индекс строки по тексту
        count = rows.count()
        src_index = None
        for i in range(count):
            if source_text.lower() in rows.nth(i).inner_text().lower():
                src_index = i
                break
        assert src_index is not None, f"Source row not found: {source_text}"

        target_index = min(src_index + positions, count - 1)
        source_row = rows.nth(src_index)
        target_row = rows.nth(target_index)

        handle = self._drag_handle_in_row(source_row)
        expect(handle).to_be_visible()
        expect(target_row).to_be_visible()

        handle.scroll_into_view_if_needed()
        target_row.scroll_into_view_if_needed()

        sb = handle.bounding_box()
        tb = target_row.bounding_box()
        assert sb and tb, "No bounding boxes for drag&drop"

        # drag&drop мышью
        self.page.mouse.move(sb["x"] + sb["width"] / 2, sb["y"] + sb["height"] / 2)
        self.page.mouse.down()

        # тянем к target row (чуть ниже середины, чтобы гарантировать "вниз")
        self.page.mouse.move(
            tb["x"] + tb["width"] / 2,
            tb["y"] + tb["height"] * 0.75,
            steps=18
        )
        self.page.mouse.up()
    """C209626"""




    """C209627"""
    def _get_row_by_ticker(self, ticker: str):
        """Внутренний метод для поиска строки, чтобы не дублировать код"""
        return self.page.locator("tr").filter(has_text=ticker).first

    @allure.step("Checks that the UP button (the first one) is locked")
    def assert_up_button_disabled(self, ticker: str):
        """Проверяет, что кнопка ВВЕРХ (первая) заблокирована"""
        row = self._get_row_by_ticker(ticker)
        # Уточняем поиск: ищем тег button внутри ячейки (td),
        # исключая th (ячейку-перетаскиватель)
        up_button = row.locator("td button").first
        expect(up_button).to_be_disabled()

    @allure.step("Checks to see if the DOWN button (the second one) is active")
    def assert_down_button_enabled(self, ticker: str):
        """Проверяет, что кнопка ВНИЗ (вторая) активна"""
        row = self._get_row_by_ticker(ticker)
        # Ищем последнюю кнопку среди всех кнопок в ячейках td
        down_button = row.locator("td button").last
        expect(down_button).to_be_enabled()

    @allure.step("Clicks the DOWN button")
    def click_down_button(self, ticker: str):
        """Кликает на кнопку ВНИЗ (вторую)"""
        row = self._get_row_by_ticker(ticker)
        down_button = row.locator("td button").last
        down_button.click()

    @allure.step("finds the line with the ticker and scrolls to it")
    def _get_row_by_ticker(self, ticker: str):
        """Находит строку с тикером и скроллит к ней"""
        row = self.page.locator("tr").filter(has_text=ticker).first
        row.scroll_into_view_if_needed()  # Авто-скролл к элементу
        return row

    @allure.step("Checks to see if the DOWN button (the last one in the row) is locked")
    def assert_down_button_disabled(self, ticker: str):
        """Проверяет, что кнопка ВНИЗ (последняя в строке) заблокирована"""
        row = self._get_row_by_ticker(ticker)
        # Ищем именно кнопку внутри ячеек td
        down_button = row.locator("td button").last
        expect(down_button).to_be_disabled()

    @allure.step("Checks whether the UP button is active")
    def assert_up_button_enabled(self, ticker: str):
        """Проверяет, что кнопка ВВЕРХ активна (используется после сдвига вниз)"""
        row = self._get_row_by_ticker(ticker)
        up_button = row.locator("td button").first
        expect(up_button).to_be_enabled()

    @allure.step("Clicks the UP button")
    def click_up_button(self, ticker: str):
        """Кликает на кнопку ВВЕРХ"""
        row = self._get_row_by_ticker(ticker)
        up_button = row.locator("td button").first
        up_button.click()

    @allure.step("Checks whether the row containing the ticker {ticker} is the first one in the table")
    def assert_row_is_at_top(self, ticker: str):
        """Проверяет, что строка с тикером является первой в таблице (индекс 0)"""
        first_row = self.page.locator("tbody tr").first
        expect(first_row).to_contain_text(ticker)

    """C209627"""









