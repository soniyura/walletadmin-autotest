from dataclasses import dataclass


@dataclass
class EditAssetData:
    asset_name: str
    token_name: str
    ticker_name: str
    decimals: int
    contract_address: str
    url_link: str
    ex_rate: str
    exrate_source_type: str
    ai_website_url: str
    ai_pool_address: str
    ai_whitepaper_url: str
    network_fee: str


@dataclass
class EditAssetDataBTC:
    asset_name: str
    nf_high_priority: int
    nf_medium_priority: int
    nf_low_priority: int