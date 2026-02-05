import re
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def banner_unpublished_changes(self): # проверка баннера о неопубликованных изменениях
        expect(self.page.get_by_text(  # использование регулярного выражения для поиска текста баннера
            re.compile(r"You have unpublished changes in .* config file\.?") # регулярное выражение для текста баннера
        )).to_be_visible() # проверка видимости текста баннера

        publish_button = self.page.get_by_role("button", name="Publish") # локатор для кнопки "Publish"
        expect(publish_button).to_be_visible() # проверка видимости кнопки "Publish"
        expect(publish_button).to_be_enabled() # проверка, что кнопка "Publish" доступна для нажатия

    def navigate_to_application_info(self): # навигация к информации о приложении
        self.page.get_by_test_id("application-info-link").click() # клик по ссылке с тестовым идентификатором "application-info-link"