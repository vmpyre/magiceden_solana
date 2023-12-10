from helpers.utility import _make_request
from config.endpoints import MAINNET_BASE_URL
from typing import Literal

class Marketplace:
    def __init__(self):
        self.base_url = MAINNET_BASE_URL

    def get_top_50_collections(self, timeRange: type[str] = Literal['1h', '1d', '7d', '30d']):
        url = f'{self.base_url}/marketplace/popular_collections?timeRange={timeRange}'
        return _make_request(url)
