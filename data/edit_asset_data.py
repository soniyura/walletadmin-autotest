from data.models import EditAssetData
from data.models import EditAssetDataBTC
from data.models import EditAssetDataURC20
from data.models import EditAssetDataSRC20



BINANCE_USD = EditAssetData(
    asset_name="Binance USD",
    token_name="Binance USD EDITED",
    ticker_name="BUSDEDITED",
    decimals=10,
    contract_address="0xe77711cff593912fd725ffb89c0d5721f08f74d",
    url_link="https://ultimia-testnet.bscscan.com/assets/type-images/svg/empty-token2.svg",
    ex_rate="USDT",
    exrate_source_type="MANUAL",
    ai_website_url="https://ultima.io/editie",
    ai_pool_address="sggw9XgTyWFXHtm2wtPXT1zofd5dvfG4Ke",
    ai_whitepaper_url="https://ultima.io/documents/en/WhitePaperUT.pdfEDITED",
    network_fee="1",
)
BINANCE_USD = [BINANCE_USD]  # type: ignore[assignment]

TRON = EditAssetData(
    asset_name="Tether TRC20",
    token_name="Tether TRC20 EDITED",
    ticker_name="USDTEDITED",
    decimals=6,
    contract_address="TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3",
    url_link="https://static.tronscan.org/production/logo/just_icon.png",
    ex_rate="USDT",
    exrate_source_type="MANUAL",
    ai_website_url="https://tron.org",
    ai_pool_address="TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3",
    ai_whitepaper_url="https://tron.org/whitepaper.pdf",
    network_fee="2",
)
TRON = [TRON]  # type: ignore[assignment]

ETH_USDC = EditAssetData(
    asset_name="USDC ERC20",
    token_name="USDC ERC20 EDITED",
    ticker_name="USDCERC20EDITED",
    decimals=8,
    contract_address="0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7237",
    url_link="https://assets.coingecko.com/coins/images/325/large/Tether2.png",
    ex_rate="USDT",
    exrate_source_type="MANUAL",
    ai_website_url="https://tron.org",
    ai_pool_address="0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7239",
    ai_whitepaper_url="https://tron.org/whitepaper.pdf",
    network_fee="0.0002",
)
ETH_USDC = [ETH_USDC]  # type: ignore[assignment]

BTC = EditAssetDataBTC(
    asset_name="Bitcoin",
    nf_high_priority=9,
    nf_medium_priority=7,
    nf_low_priority=5,
)
BTC = [BTC]  # type: ignore[assignment]


URC20 = EditAssetDataURC20(
    asset_name="VIP1 MINTER SPLIT",
    token_name="WBTC EDITED",
    ticker_name="WBTC",
    ex_rate="USDT",
    exrate_source_type="MARKET",
    ai_website_url="https://tron.org",
    ai_pool_address="UZaVpeM6fxcsnHoq8sThmL19JnGSiWKzEc",
    ai_whitepaper_url="https://tron.org/whitepaper.pdf",
    splitting_duration=700,
    daily_reward=6,
    start_block=1,
    network_fee="2",
)
URC20 = [URC20]  # type: ignore[assignment]

SRC20 = EditAssetDataSRC20(  # type: ignore[call-arg]
    asset_name="VIP SPLIT",
    token_name="VIP SPLIT EDITED",
    ticker_name="SMS",
    ex_rate="USDT",
    exrate_source_type="MARKET",
    ai_website_url="https://tron.org",
    ai_pool_address="sN9ajQXiWio9mHuooHbTv5X2igcw7DbMs8",
    ai_whitepaper_url="https://tron.org/whitepaper.pdf",
    splitting_duration=700,
    daily_reward=6,
    start_block=1,
    freezing_fee=5,
    freezing_fee_address="sN9ajQXiWio9mHuooHbTv5X2igcw7DbMs8",
    burning_fee=1,
    burning_fee_address="sN9ajQXiWio9mHuooHbTv5X2igcw7DbMs8",
    network_fee="2",
)
SRC20 = [SRC20]  # type: ignore[assignment]