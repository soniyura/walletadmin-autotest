import pytest
from pages.assets_page import AssetsPage

def test_disable_all_filters_in_one_run(login):
    page = login
    assets = AssetsPage(page)

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

