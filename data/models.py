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

@dataclass
class EditAssetDataURC20:
    asset_name: str
    token_name: str
    ticker_name: str
    ex_rate: str
    exrate_source_type: str
    ai_website_url: str
    ai_pool_address: str
    ai_whitepaper_url: str
    splitting_duration: int
    daily_reward: int
    start_block: int
    network_fee: str


@dataclass
class EditAssetDataSRC20:
    asset_name: str
    token_name: str
    ticker_name: str
    ex_rate: str
    exrate_source_type: str
    ai_website_url: str
    ai_pool_address: str
    ai_whitepaper_url: str
    splitting_duration: int
    daily_reward: int
    start_block: int
    freezing_fee: int
    freezing_fee_address: str
    burning_fee: int
    burning_fee_address: str
    network_fee: str


@dataclass
class AddAssetDataURC20:
    network_type: str
    asset_name: str
    ticker_name: str
    ex_rate: str
    exrate_source_type: str
    splitting_duration: int
    daily_reward: int
    start_block: int
    network_fee: str