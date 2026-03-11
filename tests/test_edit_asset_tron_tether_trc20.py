import pytest
from pages.assets_page_section_view import AssetsSectionView
from pages.base_page import BasePage
from pages.manage_asset import ManageAssetPage
from data.edit_asset_data import TRON


@pytest.mark.parametrize("asset_data", TRON, ids=lambda x: x.asset_name)
def test_edit_asset(login, asset_data):
    """
    C209631
    Verify ability to edit the asset TRON NETWORK block
    https://testrail.dramaco.tech/index.php?/cases/view/209631
    """
    page = login
    base_page = BasePage(page)
    manage = ManageAssetPage(page)
    assets = AssetsSectionView(page)

    manage.enable_network_filter("TRON")
    manage.assert_network_card_visible("TRON")

    assets.open_token(asset_data.asset_name)


    manage.edit_token_name(asset_data.token_name) \
        .edit_ticker_name(asset_data.ticker_name) \
        .edit_input_int(asset_data.decimals) \
        .edit_contract_address(asset_data.contract_address) \
        .edit_url_link(asset_data.url_link) \
        .edit_ex_rate(asset_data.ex_rate) \
        .edit_exrate_source_type(asset_data.exrate_source_type) \
        .check_asset_information_switcher() \
        .edit_ai_website_url(asset_data.ai_website_url) \
        .edit_ai_pool_address(asset_data.ai_pool_address) \
        .edit_ai_whitepaper_url(asset_data.ai_whitepaper_url) \
        .next_btn_click() \
        .edit_network_fee(asset_data.network_fee) \
        .save_btn_click()



    manage.assert_num_or_str_in_confirm_modal(asset_data.token_name) \
        .assert_num_or_str_in_confirm_modal(asset_data.ticker_name) \
        .assert_num_or_str_in_confirm_modal(asset_data.decimals) \
        .assert_num_or_str_in_confirm_modal(asset_data.contract_address) \
        .assert_link_in_confirm_modal(asset_data.url_link) \
        .assert_num_or_str_in_confirm_modal(asset_data.exrate_source_type) \
        .assert_num_or_str_in_confirm_modal(asset_data.network_fee) \
        .assert_link_in_confirm_modal(asset_data.ai_website_url) \
        .assert_num_or_str_in_confirm_modal(asset_data.ai_pool_address) \
        .assert_link_in_confirm_modal(asset_data.ai_whitepaper_url) \
        .confirm_btn_click()

    base_page.banner_unpublished_changes()
    # page.pause()