from pages.login_page import LoginPage
from pages.assets_page import AssetsPage

def test_assets_page_loaded(login):
    page = login
    assets = AssetsPage(page)

    assets.assert_opened()
    assets.assert_network_filters_visible()
    assets.assert_not_empty()
