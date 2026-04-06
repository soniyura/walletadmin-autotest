import pytest
from pages.assets_page_section_view import AssetsSectionView
from pages.base_page import BasePage
from pages.manage_asset import ManageAssetPage
from pages.assets_page import AssetsPage
from data.edit_asset_data import AddURC20
import allure


@pytest.mark.parametrize("asset_data", AddURC20, ids=lambda x: x.asset_name)
@allure.title("Verify ability to add a new asset")
@allure.testcase("https://testrail.dramaco.tech/index.php?/cases/view/209628",
                 "C209628: Verify ability to add a new asset")
def test_add_new_asset(login, asset_data):
    """
    C209628
    Verify ability to add a new asset
    https://testrail.dramaco.tech/index.php?/cases/view/209628
    """

    page = login
    base_page = BasePage(page)
    manage = ManageAssetPage(page)
    assets = AssetsSectionView(page)
    assets_page = AssetsPage(page)

    assets_page.open_add_new_asset()

    manage.select_network(asset_data.network_type) \
        .edit_token_name(asset_data.asset_name) \
        .edit_ticker_name_urc20(asset_data.ticker_name) \
        .select_ticker_name(asset_data.ticker_name) \
        .edit_ex_rate(asset_data.ex_rate) \
        .edit_exrate_source_type_market(asset_data.exrate_source_type) \
        .next_btn_click() \
        .check_asset_splitting_switcher() \
        .edit_split_duration(asset_data.splitting_duration) \
        .edit_daily_reward(asset_data.daily_reward) \
        .edit_start_block(asset_data.start_block) \
        .edit_network_fee_new(asset_data.network_fee) \
        .save_btn_click()

    manage.assert_num_or_str_in_confirm_modal(asset_data.asset_name) \
        .assert_num_or_str_in_confirm_modal(asset_data.ticker_name) \
        .assert_num_or_str_in_confirm_modal(asset_data.exrate_source_type) \
        .assert_num_or_str_in_confirm_modal(asset_data.splitting_duration) \
        .assert_num_or_str_in_confirm_modal(asset_data.daily_reward) \
        .assert_num_or_str_in_confirm_modal(asset_data.start_block) \
        .assert_num_or_str_in_confirm_modal(asset_data.network_fee) \
        .confirm_btn_click()

    base_page.banner_unpublished_changes()
    # page.pause()
