import os
import pytest
import allure
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL")
    if not url:
        pytest.fail("BASE_URL is not set")
    return url

@pytest.fixture(scope="session")
def creds():
    username = os.getenv("ADMIN_USER")
    password = os.getenv("ADMIN_PASS")
    if not username or not password:
        pytest.fail("ADMIN_USER / ADMIN_PASS are not set in env/.env")
    return {"username": username, "password": password}

@pytest.fixture
def login(page, base_url, creds):
    LoginPage(page).login(creds["username"], creds["password"], base_url)
    return page


# добавление скриншотов ошибок в репорт
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        if 'login' in item.funcargs:
            # Берем объект page из твоей фикстуры login
            page = item.funcargs['login']

            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )