from pages.assets_page_section_view import AssetsSectionView


def test_assets_page_search(login):
    """
    C209625
    Verify ability to search by token name and token ticker
    https://testrail.dramaco.tech/index.php?/cases/view/209625
    """
    page = login
    assets_elem = AssetsSectionView(page)
    asset_name = "SPLIT"
    asset_tikker = "USDT"

    assets_elem.insert_asset_name(asset_name)
    assets_elem.expect_search_button_visible("Search")
    assets_elem.expect_search_button_visible("Clear")
    assets_elem.click_button("Search")
    assets_elem.assert_all_assets_contain_keyword(asset_name, field_type="name")

    assets_elem.insert_asset_name(asset_tikker)
    assets_elem.click_button("Search")
    assets_elem.assert_all_assets_contain_keyword(asset_tikker, field_type="ticker")

    # page.pause()