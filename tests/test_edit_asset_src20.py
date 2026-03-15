import pytest
from pages.assets_page_section_view import AssetsSectionView
from pages.base_page import BasePage
from pages.manage_asset import ManageAssetPage
from data.edit_asset_data import SRC20


@pytest.mark.parametrize("asset_data", SRC20, ids=lambda x: x.asset_name)
def test_edit_asset(login, asset_data):
    """
    C209629
    Verify ability to edit the token SMART NETWORK block
    https://testrail.dramaco.tech/index.php?/cases/view/209629
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
        .check_pool_fee_switcher() \
        .edit_pool_fee_percent(asset_data.freezing_fee) \
        .edit_pool_fee_address(asset_data.freezing_fee_address) \
        .check_burn_fee_switcher() \
        .edit_burn_fee_percent(asset_data.burning_fee) \
        .edit_burn_fee_address(asset_data.burning_fee_address) \
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
        .assert_num_or_str_in_confirm_modal(asset_data.freezing_fee) \
        .assert_num_or_str_in_confirm_modal(asset_data.freezing_fee_address) \
        .assert_num_or_str_in_confirm_modal(asset_data.burning_fee) \
        .assert_num_or_str_in_confirm_modal(asset_data.burning_fee_address) \
        .confirm_btn_click()

    base_page.banner_unpublished_changes()
    # page.pause()