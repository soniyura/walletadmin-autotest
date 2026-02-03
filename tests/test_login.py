from pages.login_page import LoginPage
from pages.assets_page import AssetsPage

def test_assets_page_loaded(page, base_url, creds):
    login = LoginPage(page)
    assets = AssetsPage(page)

    login.login(creds["username"], creds["password"], base_url)

    assets.assert_opened()
    assets.assert_network_filters_visible()
    assets.assert_not_empty()
