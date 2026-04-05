from playwright.sync_api import Page, expect
import allure


class AssetsPage:
    def __init__(self, page: Page):
        self.page = page

    # общие кнопки режимов
    @allure.step("Сlick the Table View button")
    def open_table_view(self):
        self.page.get_by_role("button", name="Table View").click()


    @allure.step("Сlick the Section View button")
    def open_section_view(self):
        self.page.get_by_role("button", name="Section View").click()


    @allure.step("Сlick the Sorting Mode button")
    def open_sorting_mode(self):
        self.page.get_by_role("button", name="Sorting Mode").click()


    @allure.step("Сlick the Add Asset button")
    def open_add_new_asset(self):
        # self.page.get_by_role("button", name="Add Asset").click()
        self.page.get_by_role("link", name="Add Asset").click()



