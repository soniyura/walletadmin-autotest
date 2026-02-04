from pages.app_info_page import AndroidBlock
from pages.base_page import BasePage

def test_update_android_version_info(login):
    page = login
    android_block = AndroidBlock(page)
    base_page = BasePage(page)

    base_page.navigate_to_application_info()
    android_block.update_version_info(
        current_version_code="4858",
        current_version_name="1.26.1",
        min_version_code="4857",
        min_version_name="1.26.1"
    )
    base_page.banner_unpublished_changes()
