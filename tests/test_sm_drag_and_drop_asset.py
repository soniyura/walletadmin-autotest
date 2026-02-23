from pages.assets_page_sorting_mode import AssetsSortingMode
from pages.assets_page import AssetsPage
from pages.base_page import BasePage


def test_drag_and_drop_asset(login):
    """
    C209626
    Verify ability to change the order of assets
    https://testrail.dramaco.tech/index.php?/cases/view/209626
    """
    page = login
    assets_page = AssetsPage(page)
    sort_mode = AssetsSortingMode(page)
    base_page = BasePage(page)

    assets_page.open_sorting_mode()
    sort_mode.drag_row_down("UChain", positions=1)
    base_page.banner_unpublished_changes()
    # page.pause()