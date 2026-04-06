from pages.app_info_page import OsBlock
from pages.base_page import BasePage
import allure



@allure.title("Verify ability to edit Android block")
@allure.testcase("https://testrail.dramaco.tech/index.php?/cases/view/209618",
                 "C209618: Verify ability to edit Android block")
def test_update_android_version_info(login):
    """
    C209618
    Verify ability to edit Android block
    https://testrail.dramaco.tech/index.php?/cases/view/209618
    """
    page = login
    android_block = OsBlock(page)
    base_page = BasePage(page)

    base_page.navigate_to_application_info()
    android_block.update_android_version_info(
        current_version_code="4858",
        current_version_name="1.26.1",
        min_version_code="4857",
        min_version_name="1.26.1"
    )
    base_page.banner_unpublished_changes()
