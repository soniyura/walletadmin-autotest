from pages.login_page import LoginPage
from pages.assets_page import AssetsPage

def test_assets_page_loaded(login): # тест для проверки загрузки страницы активов
    page = login # получение страницы после входа
    assets = AssetsPage(page) # создание объекта страницы активов

    assets.assert_opened() # проверка открытия страницы активов
    assets.assert_network_filters_visible() # проверка видимости фильтров сетей
    assets.assert_not_empty() # проверка, что страница не пуста
