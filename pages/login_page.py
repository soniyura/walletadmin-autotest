from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    """
    C209617
    Verify ability to log in
    https://testrail.dramaco.tech/index.php?/cases/view/209617
    """
    def login(self, username: str, password: str, base_url: str): # метод для входа в систему
        self.page.goto(f"{base_url}/login") # переход на страницу входа
        self.page.get_by_test_id("username-input").fill(username) # заполнение поля имени пользователя
        self.page.get_by_test_id("password-input").fill(password) # заполнение поля пароля
        self.page.get_by_test_id("sign-in-button").click() # клик по кнопке входа
        self.page.get_by_role("button", name="Download").click() # клик по кнопке "Download" после входа


