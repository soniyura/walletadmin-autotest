from pages.assets_page_sorting_mode import AssetsSortingMode
from pages.assets_page import AssetsPage
from pages.base_page import BasePage
import allure


@allure.title("Verify ability to move the asset up/down")
@allure.testcase("https://testrail.dramaco.tech/index.php?/cases/view/209627",
              "C209619 :Verify ability to move the asset up/down")
def test_move_asset_up_down(login):
    """
    C209627
    Verify ability to move the asset up/down
    https://testrail.dramaco.tech/index.php?/cases/view/209627
    """
    page = login
    assets_page = AssetsPage(page)
    sort_mode = AssetsSortingMode(page)
    base_page = BasePage(page)

    assets_page.open_sorting_mode()

    # --- ШАГ 1: ПРОВЕРКА В ИСХОДНОЙ ТОЧКЕ (ВВЕРХУ) ---
    # У первой строки кнопка "Вверх" ДОЛЖНА быть заблокирована
    sort_mode.assert_up_button_disabled("UCN")
    sort_mode.assert_down_button_enabled("UCN")

    # --- ШАГ 2: ПЕРЕМЕЩЕНИЕ ВНИЗ ---
    sort_mode.click_down_button("UCN")
    # Ждем появления баннера (как в вашем коде)
    base_page.banner_unpublished_changes()

    # --- ШАГ 3: ПРОВЕРКА ПОСЛЕ ПЕРЕМЕЩЕНИЯ ---
    # ТЕПЕРЬ кнопка "Вверх" ДОЛЖНА быть АКТИВНА, так как над UCN кто-то есть
    sort_mode.assert_up_button_enabled("UCN")

    # Если UCN переместился в самый низ списка:
    # sort_mode.assert_down_button_disabled("UCN")

    # --- ШАГ 4: ВОЗВРАТ НАЗАД ---
    sort_mode.click_up_button("UCN")

    # --- ШАГ 5: ФИНАЛЬНАЯ ПРОВЕРКА ---
    # Теперь UCN снова вверху, кнопка "Вверх" снова заблокирована
    sort_mode.assert_up_button_disabled("UCN")

    # page.pause()