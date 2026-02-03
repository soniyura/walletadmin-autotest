from pages.app_info_page import IosBlock
from pages.nav_menu import NavMenu
from pages.notify_updata_config import Notify_updata_config


def test_update_android_version_info(login):
    page = login
    nav_menu = NavMenu(page)
    ios_block = IosBlock(page)
    notify = Notify_updata_config(page)

    nav_menu.navigate_to_application_info()
    ios_block.update_version_info(
        current_version_name="1.26.1",
        min_version_name="1.26.1"
    )
    notify.banner_unpublished_changes()
