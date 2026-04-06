from pages.base_page import BasePage
from pages.assets_page_section_view import AssetsSectionView
from pages.manage_asset import ManageAssetPage
from pages.assets_page import AssetsPage
from pages.assets_page_table_view import AssetsTableView
import allure



@allure.title("Аsset shutdown")
@allure.testcase("https://testrail.dramaco.tech/index.php?/cases/view/209623",
                 "C209623: Аsset shutdown")
def test_asset_shutdown(login):
    """
    C209623
    Аsset shutdown
    https://testrail.dramaco.tech/index.php?/cases/view/209623
    """
    page = login
    assets = AssetsSectionView(page)
    base_page = BasePage(page)
    manage = ManageAssetPage(page)
    assets_page = AssetsPage(page)
    table = AssetsTableView(page)
    asset_name = "ULTIMA URC-20"


    assets.disable_token(asset_name)
    base_page.banner_unpublished_changes()
    assets.open_token(asset_name)
    manage.assert_opened_manage_asset_page()
    manage.assert_default_state_switch_off()
    manage.cancel_btn_click()
    assets_page.open_table_view()
    table.assert_asset_switch_off(asset_name)
    # page.pause()



