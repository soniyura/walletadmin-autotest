from pages.app_info_page import AndroidBlock
from pages.nav_menu import NavMenu
from pages.notify_updata_config import Notify_updata_config


def test_update_android_version_info(login):
    page = login
    nav_menu = NavMenu(page)
    android_block = AndroidBlock(page)
    notify = Notify_updata_config(page)

    nav_menu.navigate_to_application_info()
    android_block.update_version_info(
        current_version_code="4858",
        current_version_name="1.26.1",
        min_version_code="4857",
        min_version_name="1.26.1"
    )
    notify.banner_unpublished_changes()
