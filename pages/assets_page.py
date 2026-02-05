import re
from playwright.sync_api import Page, expect

class AssetsPage:
    def __init__(self, page: Page): # создание конструктора класса
        self.page = page # инициализация страницы

    # login test
    def assert_opened(self): # проверка открытия страницы
        expect(self.page).to_have_url(re.compile(r".*/assets/?(\?.*)?$")) # проверка URL
        expect(self.page.get_by_text("Assets", exact=True)).to_be_visible() # проверка видимости текста "Assets"

    def assert_network_filters_visible(self): # проверка видимости фильтров сетей
        filters = self.page.locator("form") # локатор для формы фильтров

        networks = ["SMARTCHAIN", "ULTIMA", "UCHAIN", "SMART", "TRON", "ETHEREUM", "BITCOIN"] # список сетей
        for n in networks: # цикл по сетям
            loc = filters.get_by_text(n, exact=True) # локатор для каждой сети
            expect(loc.first).to_be_visible() # проверка видимости локатора

    def assert_not_empty(self): # проверка, что страница не пуста
        switches = self.page.locator('[role="switch"], input[type="checkbox"]') # локатор для переключателей
        expect(switches.first).to_be_visible() # проверка видимости первого переключателя
        assert switches.count() > 0 # проверка, что количество переключателей больше нуля



    # enable/disable assets/network

    def _network_filter(self, network: str): # вспомогательный метод для получения локатора фильтра по сети
        # Берём чекбокс по тексту сети (SMARTCHAIN, ULTIMA...)
        # Поднимаемся на уровень вверх — там контейнер с checkbox + текст
        return self.page.get_by_text(network, exact=True).locator("..") # локатор для контейнера с чекбоксом и текстом

    def disable_network_filter(self, network: str): # метод для отключения фильтра по сети
        filter_item = self._network_filter(network) # получение локатора фильтра по сети

        checkbox_input = filter_item.locator("input[type='checkbox']").first # локатор для чекбокса
        checkbox_ui = filter_item.locator("span.MuiCheckbox-root").first # локатор для UI элемента чекбокса

        expect(checkbox_input).to_be_visible() # проверка видимости чекбокса

        if checkbox_input.is_checked(): # если чекбокс отмечен
            checkbox_ui.click()  # <-- ВАЖНО: кликаем по MuiCheckbox-root элементу, а не по самому input
            expect(checkbox_input).not_to_be_checked() # проверка, что чекбокс не отмечен

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

    def assert_network_card_visible(self, network: str): # метод для проверки видимости карточки сети
        expect(self.network_card(network)).to_be_visible() # проверка видимости карточки сети

    def assert_network_card_hidden(self, network: str): # метод для проверки скрытости карточки сети
        expect(self.network_card(network)).to_be_hidden() #

    # ---------- PLACEHOLDER ----------

    def assert_unassigned_visible(self): # метод для проверки видимости плейсхолдера "Unassigned Space"
        expect(
            self.page.get_by_text("Unassigned Space", exact=True).first     # локатор по тексту "Unassigned Space"
        ).to_be_visible()






