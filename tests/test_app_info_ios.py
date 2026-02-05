from pages.app_info_page import OsBlock
from pages.base_page import BasePage


def test_update_android_version_info(login):
    page = login
    ios_block = OsBlock(page)
    base_page = BasePage(page)

    base_page.navigate_to_application_info()
    ios_block.update_ios_version_info(
        current_version_name="1.26.1",
        min_version_name="1.26.1"
    )
    base_page.banner_unpublished_changes()
