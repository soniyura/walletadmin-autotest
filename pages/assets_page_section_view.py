import re
from playwright.sync_api import Page, expect
from pages.manage_asset import ManageAssetPage
import allure

class AssetsSectionView:
    def __init__(self, page: Page): # создание конструктора класса
        self.page = page # инициализация страницы

    # login test
    @allure.step("Check if the Assets page opens")
    def assert_opened(self): # проверка открытия страницы
        expect(self.page).to_have_url(re.compile(r".*/assets/?(\?.*)?$")) # проверка URL
        expect(self.page.get_by_text("Assets", exact=True)).to_be_visible() # проверка видимости текста "Assets"

    @allure.step("Check the filters for the displayed networks ")
    def assert_network_filters_visible(self): # проверка видимости фильтров сетей
        filters = self.page.locator("form") # локатор для формы фильтров

        networks = ["SMARTCHAIN", "ULTIMA", "UCHAIN", "SMART", "TRON", "ETHEREUM", "BITCOIN"] # список сетей
        for n in networks: # цикл по сетям
            loc = filters.get_by_text(n, exact=True) # локатор для каждой сети
            expect(loc.first).to_be_visible() # проверка видимости локатора

    @allure.step("check that the page isn't empty")
    def assert_not_empty(self): # проверка, что страница не пуста
        switches = self.page.locator('[role="switch"], input[type="checkbox"]') # локатор для переключателей
        expect(switches.first).to_be_visible() # проверка видимости первого переключателя
        assert switches.count() > 0 # проверка, что количество переключателей больше нуля



    # enable/disable assets/network

    def _network_filter(self, network: str): # вспомогательный метод для получения локатора фильтра по сети
        # Берём чекбокс по тексту сети (SMARTCHAIN, ULTIMA...)
        # Поднимаемся на уровень вверх — там контейнер с checkbox + текст
        return self.page.get_by_text(network, exact=True).locator("..") # локатор для контейнера с чекбоксом и текстом

    @allure.step("disable the network filter : {network}")
    def disable_network_filter(self, network: str): # метод для отключения фильтра по сети
        filter_item = self._network_filter(network) # получение локатора фильтра по сети

        checkbox_input = filter_item.locator("input[type='checkbox']").first # локатор для чекбокса
        checkbox_ui = filter_item.locator("span.MuiCheckbox-root").first # локатор для UI элемента чекбокса

        expect(checkbox_input).to_be_visible() # проверка видимости чекбокса

        if checkbox_input.is_checked(): # если чекбокс отмечен
            checkbox_ui.click()  # <-- ВАЖНО: кликаем по MuiCheckbox-root элементу, а не по самому input
            expect(checkbox_input).not_to_be_checked() # проверка, что чекбокс не отмечен

    @allure.step("Enable the network filter : {network}")
    def enable_network_filter(self, network: str): # метод для включения фильтра по сети
        filter_item = self._network_filter(network) # получение локатора фильтра по сети

        checkbox_input = filter_item.locator("input[type='checkbox']").first # локатор для чекбокса
        checkbox_ui = filter_item.locator("span.MuiCheckbox-root").first # локатор для UI элемента чекбокса

        expect(checkbox_input).to_be_visible() # проверка видимости чекбокса

        if not checkbox_input.is_checked(): # если чекбокс не отмечен
            checkbox_ui.click() # <-- ВАЖНО: кликаем по MuiCheckbox-root элементу, а не по самому input
            expect(checkbox_input).to_be_checked() # проверка, что чекбокс отмечен

    # ---------- CARDS ----------

    def network_card(self, network: str): # метод для получения локатора карточки сети
        title = f"{network} NETWORK" # формирование заголовка карточки
        return ( # возврат локатора карточки по заголовку
            self.page
            .get_by_text(title, exact=True)    # локатор по тексту заголовка
            .locator("xpath=ancestor::div[contains(@class,'MuiBox-root')][1]") # поднимаемся к родительскому div с классом MuiBox-root
        )

    @allure.step("check Network card visibility: {network}")
    def assert_network_card_visible(self, network: str): # метод для проверки видимости карточки сети
        expect(self.network_card(network)).to_be_visible() # проверка видимости карточки сети

    @allure.step("check Network card hidden : {network}")
    def assert_network_card_hidden(self, network: str): # метод для проверки скрытости карточки сети
        expect(self.network_card(network)).to_be_hidden() #

    # ---------- PLACEHOLDER ----------

    @allure.step("Check what's displayed: Unassigned Space")
    def assert_unassigned_visible(self): # метод для проверки видимости плейсхолдера "Unassigned Space"
        expect(
            self.page.get_by_text("Unassigned Space", exact=True).first     # локатор по тексту "Unassigned Space"
        ).to_be_visible()

    """
    C209623
    Аsset shutdown
    https://testrail.dramaco.tech/index.php?/cases/view/209623
    """
    def _token_row_by_name(self, token_name: str):
        """
        Находим строку/карточку токена по имени (например 'ULTIMA URC-20')
        и поднимаемся к ближайшему контейнеру строки, внутри которого есть свитч.
        """
        name = self.page.get_by_text(token_name, exact=True).first
        expect(name).to_be_visible()

        # Поднимаемся к ближайшему контейнеру строки.
        # Обычно у MUI это ближайший div.MuiBox-root, в котором есть switch.
        row = name.locator(
            "xpath=ancestor::div[contains(@class,'MuiBox-root')][.//span[contains(@class,'MuiSwitch-root')] or .//input[@type='checkbox']][1]"
        )
        return row



    @allure.step("Disable the token: {token_name}")
    def disable_token(self, token_name: str):
        row = self._token_row_by_name(token_name)
        checkbox = row.locator("input[type='checkbox']").first
        switch_ui = row.locator("span.MuiSwitch-root").first
        expect(checkbox).to_be_visible()
        # если включен — выключаем
        if checkbox.is_checked():
            switch_ui.click()
            expect(checkbox).not_to_be_checked()
        else:
            # уже выключен — ок
            expect(checkbox).not_to_be_checked()


    @allure.step("Finds the token block by name and clicks on it : {token_name}")
    def open_token(self, token_name: str):
        """
        Находит блок токена по имени и кликает по тексту токена внутри этого блока.
        """
        row = self._token_row_by_name(token_name)
        # клик именно по тексту внутри найденного блока (самый стабильный вариант)
        token_link = row.get_by_text(token_name, exact=True).first
        expect(token_link).to_be_visible()
        token_link.click()


    """
    C209625
    Verify ability to search by token name and token ticker
    https://testrail.dramaco.tech/index.php?/cases/view/209625    
    """
    @allure.step("Type the text into the search field: {text} ")
    def insert_asset_name(self, text: str):
        search_input = self.page.locator("input#search")
        search_input.clear()
        search_input.fill(text)

    # метод для     проверки видимости и доступности кнопки поиска
    @allure.step("Checking the button display: {button_name} ")
    def expect_search_button_visible(self, button_name: str):
        expect(
            self.page.get_by_role("button", name=button_name)
        ).to_be_visible()
        expect(
            self.page.get_by_role("button", name=button_name)
        ).to_be_enabled()

    @allure.step("Click the button : {button_name} ")
    def click_button(self, button_name: str):
        button = self.page.get_by_role("button", name=button_name, exact=True)
        expect(button).to_be_visible()
        expect(button).to_be_enabled()
        button.click()

    """
    Метод для проверки, что все отображаемые активы (в зависимости от фильтра) 
    содержат заданное ключевое слово в имени или тикере.
    то есть если 
    field_type="name", то проверяем, что keyword(передаваемое слово например SPLIT ищется по имени) 
    есть в имени каждого актива, если 
    field_type="ticker", то проверяем, что keyword(передаваемое слово например USDT ищется по тикеру) 
    есть в тикере каждого актива.
    """

    @allure.step("Verify that all displayed assets contain the keyword in their name or ticker")
    def assert_all_assets_contain_keyword(
            self,
            keyword: str,
            field_type: str = "name"  # name | ticker
    ):
        self.page.wait_for_load_state("networkidle")

        # выбираем нужный класс
        typography_class = {
            "name": "MuiTypography-body1",
            "ticker": "MuiTypography-body2"
        }.get(field_type)

        assert typography_class, f"Unknown field_type: {field_type}"

        elements = self.page.locator(
            f"div.MuiBox-root:has(span.MuiSwitch-root) p.{typography_class}"
        )

        expect(elements.first).to_be_visible()

        texts = [
            t.strip()
            for t in elements.all_text_contents()
            if t and t.strip()
        ]

        assert texts, "No values found after search"

        kw = keyword.lower()
        bad = [t for t in texts if kw not in t.lower()]

        assert not bad, (
            f"Some values do not contain '{keyword}': {bad[:5]} "
            f"(total bad: {len(bad)}, total values: {len(texts)})"
        )
    """C209625"""









