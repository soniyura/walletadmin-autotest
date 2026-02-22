from playwright.sync_api import Page, expect

class OsBlock:
    def __init__(self, page: Page):
        self.page = page

    """
    C209618
    Verify ability to edit Android block
    https://testrail.dramaco.tech/index.php?/cases/view/209618
    """
    def update_android_version_info(self, current_version_code: str, current_version_name: str,
                            min_version_code: str, min_version_name: str): # обновление информации о версии Android
        self.page.locator("form").filter(has_text="AndroidApplication").get_by_role("button").click() # открытие формы редактирования

        self.page.get_by_role("textbox", name="Current Version Code").fill(current_version_code) # заполнение текущего кода версии
        self.page.get_by_role("textbox", name="Current Version Name").fill(current_version_name) # заполнение текущего имени версии
        self.page.get_by_role("textbox", name="MIN Version Code").fill(min_version_code) # заполнение минимального кода версии
        self.page.get_by_role("textbox", name="MIN Version Name").fill(min_version_name) #

        self.page.get_by_role("button", name="Confirm").click() # подтверждение изменений

        expect(self.page.get_by_text(current_version_code)).to_be_visible() # проверка видимости текущего кода версии
        expect(self.page.get_by_text(current_version_name).first).to_be_visible() # проверка видимости текущего имени версии
        expect(self.page.get_by_text(min_version_code)).to_be_visible() # проверка видимости минимального кода версии
        expect(self.page.get_by_text(min_version_name).nth(1)).to_be_visible() # проверка видимости минимального имени версии

        self.page.get_by_role("button", name="Confirm").click() # окончательное подтверждение изменений


    """
    C209619
    Verify ability to edit iOS block
    https://testrail.dramaco.tech/index.php?/cases/view/209619
    """
    def update_ios_version_info(self, current_version_name: str, min_version_name: str): # обновление информации о версии iOS
        self.page.locator("form").filter(has_text="IosApplication").get_by_role("button").click() # открытие формы редактирования

        self.page.get_by_role("textbox", name="Current Version Name").fill(current_version_name) # заполнение текущего имени версии
        self.page.get_by_role("textbox", name="MIN Version Name").fill(min_version_name)  # заполнение минимального имени версии

        self.page.get_by_role("button", name="Confirm").click() # подтверждение изменений

        expect(self.page.get_by_text(current_version_name).first).to_be_visible() # проверка видимости текущего имени версии
        expect(self.page.get_by_text(min_version_name).nth(1)).to_be_visible() # проверка видимости минимального имени версии

        self.page.get_by_role("button", name="Confirm").click() # окончательное подтверждение изменений


