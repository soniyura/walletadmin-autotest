from playwright.sync_api import Page, expect
import allure

class ManageAssetPage:
    def __init__(self, page: Page):
        self.page = page

    ID_TOKEN_NAME = 'input[name="name"]'
    ID_TICKER_NAME = 'input[name="abbr"]'
    ID_TICKER_NAME_URC20 = 'input[placeholder="Asset Ticker (eg BTC)"]'
    ID_DECIMALS = 'input[name="decimal_places"]'
    ID_CONTRACT_ADDRESS = 'input[name="contract_address"]'
    ID_URL = 'input[name="icon_url"]'
    ID_EXRATE = 'input[name="assets.0.to"]'
    ID_AI_WEBSITE_URL = 'input[name="website_url"]'
    ID_AI_POOL_ADDRESS = 'input[name="pool_address"]'
    ID_AI_WHITEPAPER_URL = 'input[name="whitepaper_url"]'
    ID_NETWORK_FEE = 'input[name="base_coin_min_balance"]'
    ID_NETWORK_FEE_NEW = 'input[name="max_network_fee"]'
    ID_DIALOG = '[role="dialog"]'
    ID_HIGH_PRIO_BTC = 'input[name="high_priority_btc_fee"]'
    ID_MEDIUM_PRIO_BTC = 'input[name="medium_priority_btc_fee"]'
    ID_LOW_PRIO_BTC = 'input[name="low_priority_btc_fee"]'
    ID_SPLIT_DURATION = 'input[name="split_duration"]'
    ID_DAILY_REWARD = 'input[name="daily_reward_amount"]'
    ID_START_BLOCK = 'input[name="daily_reward_start_block"]'
    ID_POOL_FEE_PERCENT = 'input[name="pool_fee_percent"]'
    ID_POOL_FEE_ADDRESS = 'input[name="pool_fee_wallet_address"]'
    ID_BURN_FEE_PERCENT = 'input[name="burn_fee_percent"]'
    ID_BURN_FEE_ADDRESS = 'input[name="burn_fee_wallet_address"]'
    ID_NETWORK_TYPE = 'input[name="network"]'


    @allure.step("Open Manage Assets")
    def assert_opened_manage_asset_page(self):
        expect(self.page.get_by_text("Manage Asset", exact=True)).to_be_visible()

    @allure.step("Сhecks that the “Default State” switch is off")
    def assert_default_state_switch_off(self):
        label = self.page.get_by_text("Default State", exact=True).first
        expect(label).to_be_visible()
        label.scroll_into_view_if_needed()
        # Ищем ближайший контейнер, в котором есть checkbox
        # (этот XPath поднимется вверх до первого предка, содержащего input[type=checkbox])
        row = label.locator("xpath=ancestor::*[.//input[@type='checkbox']][1]")
        checkbox = row.locator("input[type='checkbox']").first
        expect(checkbox).to_be_attached()   # в DOM
        # visible может быть false, если input скрытый (у MUI так бывает)
        # поэтому лучше проверять именно состояние:
        expect(checkbox).not_to_be_checked()


    @allure.step("Click the Cance button")
    def cancel_btn_click(self):
        self.page.get_by_role("link", name="Cancel").click()

    @allure.step("Click the Next button")
    def next_btn_click(self):
        self.page.get_by_text("Next", exact=True).click()
        return self

    @allure.step("Click the Save button")
    def save_btn_click(self):
        self.page.get_by_text("Save", exact=True).click()
        return self

    @allure.step("Click the Confirm button")
    def confirm_btn_click(self):
        self.page.get_by_text("Confirm", exact=True).click()
        return self

    def select_network(self, network_name: str):
        # Кликаем по элементу с ролью combobox (их может быть много, берем первый для теста)
        self.page.locator('div[role="combobox"]').first.click()
        # Выбираем сеть
        self.page.get_by_role("option", name=network_name, exact=False).click()
        return self

    def edit_input_str(self, id: str, value: str):
        self.page.locator(id).fill(value)

    @allure.step("Sets the value in the pool_fee_percent field: {value}")
    def edit_pool_fee_percent(self, value: int):
        self.edit_input_str(self.ID_POOL_FEE_PERCENT, str(value))
        return self

    @allure.step("Sets the value in the pool_fee_address field: {value}")
    def edit_pool_fee_address(self, value: str):
        self.edit_input_str(self.ID_POOL_FEE_ADDRESS, value)
        return self

    @allure.step("Sets the value in the burn_fee_percent field: {value}")
    def edit_burn_fee_percent(self, value: int):
        self.edit_input_str(self.ID_BURN_FEE_PERCENT, str(value))
        return self

    @allure.step("Sets the value in the burn_fee_address field: {value}")
    def edit_burn_fee_address(self, value: str):
        self.edit_input_str(self.ID_BURN_FEE_ADDRESS, value)
        return self

    @allure.step("Sets the value in the high_priority field: {value}")
    def edit_higt_prio_btc(self, value: int):
        self.edit_input_str(self.ID_HIGH_PRIO_BTC, str(value))
        return self

    @allure.step("Sets the value in the medium_priority field: {value}")
    def edit_medium_prio_btc(self, value: int):
        self.edit_input_str(self.ID_MEDIUM_PRIO_BTC, str(value))
        return self

    @allure.step("Sets the value in the low_priority field: {value}")
    def edit_low_prio_btc(self, value: int):
        self.edit_input_str(self.ID_LOW_PRIO_BTC, str(value))
        return self

    @allure.step("Sets the value in the token_name field: {value}")
    def edit_token_name(self, value: str):
        self.edit_input_str(self.ID_TOKEN_NAME, value)
        return self

    @allure.step("Sets the value in the ticker_name field: {value}")
    def edit_ticker_name(self, value: str):
        self.edit_input_str(self.ID_TICKER_NAME, value)
        return self

    @allure.step("Sets the value in the ticker_name_urc20 field: {value}")
    def edit_ticker_name_urc20(self, value: str):
        self.edit_input_str(self.ID_TICKER_NAME_URC20, value)
        return self

    @allure.step("Select ticker name: {ticker}")
    def select_ticker_name(self, ticker: str):
        input_locator = self.page.locator(self.ID_TICKER_NAME_URC20)
        input_locator.click()
        input_locator.fill(ticker)
        dropdown_option = self.page.locator('[role="option"]').filter(has_text=ticker).first
        expect(dropdown_option).to_be_visible()
        dropdown_option.click()
        return self

    @allure.step("Sets the value in the split_duration field: {value}")
    def edit_split_duration(self, value: str):
        self.edit_input_str(self.ID_SPLIT_DURATION, str(value))
        return self

    @allure.step("Sets the value in the daily_reward field: {value}")
    def edit_daily_reward(self, value: str):
        self.edit_input_str(self.ID_DAILY_REWARD, str(value))
        return self

    @allure.step("Sets the value in the start_block field: {value}")
    def edit_start_block(self, value: str):
        self.edit_input_str(self.ID_START_BLOCK, str(value))
        return self

    @allure.step("Sets the value in the decimals field: {value}")
    def edit_input_int(self, value: int):
        self.edit_input_str(self.ID_DECIMALS, str(value))
        return self

    @allure.step("Sets the value in the contract_address field: {value}")
    def edit_contract_address(self, value: str):
        self.edit_input_str(self.ID_CONTRACT_ADDRESS, value)
        return self

    @allure.step("Sets the value in the url_link field: {value}")
    def edit_url_link(self, value: str):
        self.edit_input_str(self.ID_URL, value)
        return self

    @allure.step("Sets the value in the ex_rate field: {value}")
    def edit_ex_rate(self, value: str):
        self.edit_input_str(self.ID_EXRATE, value)
        return self

    @allure.step("Sets the value in the exrate_source_type field")
    def edit_exrate_source_type(self, value: str):
        dropdown = self.page.get_by_role("combobox").nth(1)
        dropdown.scroll_into_view_if_needed()
        dropdown.click()
        self.page.get_by_role("option", name=value).click()
        return self

    @allure.step("Sets the value in the exrate_source_type field")
    def edit_exrate_source_type_market(self, value: str):
        dropdown = self.page.get_by_role("combobox").nth(2)
        dropdown.scroll_into_view_if_needed()
        dropdown.click()
        self.page.get_by_role("option", name=value).click()
        return self

    @allure.step("Turn ON asset_information_switcher")
    def check_asset_information_switcher(self):
        toggle = self.page.locator('input[name="about"]')
        if not toggle.is_checked():
            toggle.click()
        return self

    @allure.step("Turn ON asset_splitting_switcher")
    def check_asset_splitting_switcher(self):
        toggle = self.page.locator('input[name="splitting"]')
        if not toggle.is_checked():
            toggle.click()
        return self

    @allure.step("Turn ON pool_fee_switcher")
    def check_pool_fee_switcher(self):
        toggle = self.page.locator('input[name="pool_fee"]')
        if not toggle.is_checked():
            toggle.click()
        return self

    @allure.step("Turn ON burn_fee_switcher")
    def check_burn_fee_switcher(self):
        toggle = self.page.locator('input[name="burning_fee"]')
        if not toggle.is_checked():
            toggle.click()
        return self

    @allure.step("Sets the value in the ai_website_url field: {value}")
    def edit_ai_website_url(self, value: str):
        self.edit_input_str(self.ID_AI_WEBSITE_URL, value)
        return self

    @allure.step("Sets the value in the ai_pool_address field: {value}")
    def edit_ai_pool_address(self, value: str):
        self.edit_input_str(self.ID_AI_POOL_ADDRESS, value)
        return self

    @allure.step("Sets the value in the ai_whitepaper_url field: {value}")
    def edit_ai_whitepaper_url(self, value: str):
        self.edit_input_str(self.ID_AI_WHITEPAPER_URL, value)
        return self

    @allure.step("Sets the value in the network_fee field: {value}")
    def edit_network_fee(self, value: str):
        self.edit_input_str(self.ID_NETWORK_FEE, str(value))
        return self

    @allure.step("Sets the value in the network_fee_new field: {value}")
    def edit_network_fee_new(self, value: str):
        self.edit_input_str(self.ID_NETWORK_FEE_NEW, str(value))
        return self

    def _network_filter(self, network: str): # вспомогательный метод для получения локатора фильтра по сети
        # Берём чекбокс по тексту сети (SMARTCHAIN, ULTIMA...)
        # Поднимаемся на уровень вверх — там контейнер с checkbox + текст
        return self.page.get_by_text(network, exact=True).locator("..")

    @allure.step("Enabling the network filter: {network}")
    def enable_network_filter(self, network: str): # метод для включения фильтра по сети
        filter_item = self._network_filter(network) # получение локатора фильтра по сети

        checkbox_input = filter_item.locator("input[type='checkbox']").first # локатор для чекбокса
        checkbox_ui = filter_item.locator("span.MuiCheckbox-root").first # локатор для UI элемента чекбокса

        expect(checkbox_input).to_be_visible() # проверка видимости чекбокса

        if not checkbox_input.is_checked(): # если чекбокс не отмечен
            checkbox_ui.click() # <-- ВАЖНО: кликаем по MuiCheckbox-root элементу, а не по самому input
            expect(checkbox_input).to_be_checked() # проверка, что чекбокс отмечен
        # expect(self.network_card(network)).to_be_visible()

    @allure.step("Check that the network is turned on: {network}")
    def assert_network_card_visible(self, network: str): # метод для проверки видимости карточки сети
        expect(self.network_card(network)).to_be_visible() # проверка видимости карточки сети

    def network_card(self, network: str): # метод для получения локатора карточки сети
        title = f"{network} NETWORK" # формирование заголовка карточки
        return ( # возврат локатора карточки по заголовку
            self.page
            .get_by_text(title, exact=True)    # локатор по тексту заголовка
            .locator("xpath=ancestor::div[contains(@class,'MuiBox-root')][1]") # поднимаемся к родительскому div с классом MuiBox-root
        )

    @allure.step("Сheck that the value entered is correct : {value}")
    def assert_num_or_str_in_confirm_modal(self, value: int | str):
        modal = self.page.locator(self.ID_DIALOG)
        expect(modal).to_be_visible()
        expect(modal).to_contain_text(str(value))
        return self

    @allure.step("Сheck that the link entered is correct : {expected_href}")
    def assert_link_in_confirm_modal(self, expected_href: str):
        modal = self.page.locator(self.ID_DIALOG)
        expect(modal).to_be_visible()
        link = modal.locator(f'a[href="{expected_href}"]').first
        expect(link).to_be_visible()
        return self





















