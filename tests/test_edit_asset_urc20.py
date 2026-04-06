import pytest
from pages.assets_page_section_view import AssetsSectionView
from pages.base_page import BasePage
from pages.manage_asset import ManageAssetPage
from data.edit_asset_data import URC20
import allure


@pytest.mark.parametrize("asset_data", URC20, ids=lambda x: x.asset_name)
@allure.title("Verify ability to edit the token ULTIMA NETWORK block")
@allure.testcase("https://testrail.dramaco.tech/index.php?/cases/view/209637",
                 "C209637: Verify ability to edit the token ULTIMA NETWORK block")
def test_edit_asset(login, asset_data):
    """
    C209637
    Verify ability to edit the token ULTIMA NETWORK block
    https://testrail.dramaco.tech/index.php?/cases/view/209637
    """
    page = login
    base_page = BasePage(page)
    manage = ManageAssetPage(page)
    assets = AssetsSectionView(page)

    assets.open_token(asset_data.asset_name)

    manage.edit_token_name(asset_data.token_name) \
        .edit_ticker_name_urc20(asset_data.ticker_name) \
        .select_ticker_name(asset_data.ticker_name) \
        .edit_ex_rate(asset_data.ex_rate) \
        .edit_exrate_source_type_market(asset_data.exrate_source_type) \
        .check_asset_information_switcher() \
        .edit_ai_website_url(asset_data.ai_website_url) \
        .edit_ai_pool_address(asset_data.ai_pool_address) \
        .edit_ai_whitepaper_url(asset_data.ai_whitepaper_url) \
        .next_btn_click() \
        .edit_split_duration(asset_data.splitting_duration) \
        .edit_daily_reward(asset_data.daily_reward) \
        .edit_start_block(asset_data.start_block) \
        .edit_network_fee_new(asset_data.network_fee) \
        .save_btn_click()

    manage.assert_num_or_str_in_confirm_modal(asset_data.token_name) \
        .assert_num_or_str_in_confirm_modal(asset_data.ticker_name) \
        .assert_num_or_str_in_confirm_modal(asset_data.exrate_source_type) \
        .assert_link_in_confirm_modal(asset_data.ai_website_url) \
        .assert_num_or_str_in_confirm_modal(asset_data.ai_pool_address) \
        .assert_link_in_confirm_modal(asset_data.ai_whitepaper_url) \
        .assert_num_or_str_in_confirm_modal(asset_data.splitting_duration) \
        .assert_num_or_str_in_confirm_modal(asset_data.daily_reward) \
        .assert_num_or_str_in_confirm_modal(asset_data.start_block) \
        .assert_num_or_str_in_confirm_modal(asset_data.network_fee) \
        .confirm_btn_click()

    base_page.banner_unpublished_changes()
    # page.pause()