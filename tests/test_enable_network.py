from pages.assets_page_section_view import AssetsSectionView

def test_disable_all_filters_in_one_run(login):
    """
    C209622
    Verify block disabling from the Assets page
    https://testrail.dramaco.tech/index.php?/cases/view/209622
    """
    page = login
    assets = AssetsSectionView(page)

    networks = ["SMARTCHAIN", "ULTIMA", "UCHAIN", "SMART"]

    # выключаем по очереди и проверяем
    for n in networks:
        assets.assert_network_card_visible(n)
        assets.disable_network_filter(n)
        assets.assert_network_card_hidden(n)
        assets.assert_unassigned_visible()

    # включаем обратно (чтобы другие тесты не зависели)
    for n in networks:
        assets.enable_network_filter(n)
        assets.assert_network_card_visible(n)