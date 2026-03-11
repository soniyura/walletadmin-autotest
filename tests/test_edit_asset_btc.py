import pytest
from pages.assets_page_section_view import AssetsSectionView
from pages.base_page import BasePage
from pages.manage_asset import ManageAssetPage
from data.edit_asset_data import BTC


@pytest.mark.parametrize("asset_data", BTC, ids=lambda x: x.asset_name)
def test_edit_asset(login, asset_data):
    """
    C209639
    Verify ability to edit the asset BITCOIN NETWORK block
    https://testrail.dramaco.tech/index.php?/cases/view/209639
    """
    page = login
    base_page = BasePage(page)
    manage = ManageAssetPage(page)
    assets = AssetsSectionView(page)

    manage.enable_network_filter("BITCOIN")
    manage.assert_network_card_visible("BITCOIN")

    assets.open_token(asset_data.asset_name)

    manage.edit_higt_prio_btc(asset_data.nf_high_priority) \
        .edit_medium_prio_btc(asset_data.nf_medium_priority) \
        .edit_low_prio_btc(asset_data.nf_low_priority) \
        .save_btn_click()

    manage.assert_num_or_str_in_confirm_modal(asset_data.nf_high_priority) \
        .assert_num_or_str_in_confirm_modal(asset_data.nf_medium_priority) \
        .assert_num_or_str_in_confirm_modal(asset_data.nf_low_priority) \
        .confirm_btn_click()

    base_page.banner_unpublished_changes()
    # page.pause()