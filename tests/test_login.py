from pages.assets_page_section_view import AssetsSectionView

def test_assets_page_loaded(login): # тест для проверки загрузки страницы активов
    """
    C209617
    Verify ability to log in
    https://testrail.dramaco.tech/index.php?/cases/view/209617
    """
    page = login # получение страницы после входа
    assets = AssetsSectionView(page) # создание объекта страницы активов

    assets.assert_opened() # проверка открытия страницы активов
    assets.assert_network_filters_visible() # проверка видимости фильтров сетей
    assets.assert_not_empty() # проверка, что страница не пуста
