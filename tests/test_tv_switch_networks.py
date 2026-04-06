from pages.assets_page_table_view import AssetsTableView
from pages.assets_page import AssetsPage
import allure


@allure.title("Verify ability to switch between networks")
@allure.testcase("https://testrail.dramaco.tech/index.php?/cases/view/209624",
                 "C209624: Verify ability to switch between networks")
def test_assets_page_table_view(login):
    """
    C209624
    Verify ability to switch between networks
    https://testrail.dramaco.tech/index.php?/cases/view/209624
    """
    page = login
    assets_page = AssetsPage(page)
    table = AssetsTableView(page)

    network_ticker = {
        "SMARTCHAIN NETWORK": "BNB",
        "ULTIMA NETWORK": "ULTIMA",
        "UCHAIN NETWORK": "UCN",
        "SMART NETWORK": "SMART",
        "TRON NETWORK": "TRX",
        "ETHEREUM NETWORK": "ETH",
        "BITCOIN NETWORK": "BTC",
    }

    assets_page.open_table_view()
    table.assert_network_dropdown_default_all()

    for network, ticker in network_ticker.items():
        table.open_networks_dropdown()
        table.click_network_option(network)
        table.assert_table_has_ticker(ticker)

    # page.pause()