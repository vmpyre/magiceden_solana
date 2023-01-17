from helpers.utility import _make_request
from config.endpoints import MAINNET_BASE_URL

class Collections:
    def __init__(self):
        self.base_url = MAINNET_BASE_URL

    def get_collections(self, offset=0, limit=200):
        """
        Retrieves collections.

        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 200.
        :type limit: int, optional
        :return: A dictionary containing the collections.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/collections?offset={offset}&limit={limit}'
        return _make_request(url)

    def get_collection_listings(self, symbol, offset=0, limit=20):
        """
        Retrieves listings of a collection by symbol.

        :param symbol: The symbol of the collection to retrieve listings for.
        :type symbol: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 20.
        :type limit: int, optional
        :return: A dictionary containing the listings of the collection.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/collections/{symbol}/listings?offset={offset}&limit={limit}'
        return _make_request(url)

    def get_collection_activities(self, symbol, offset=0, limit=100):
        """
        Retrieves activities of a collection by symbol.

        :param symbol: The symbol of the collection to retrieve activities for.
        :type symbol: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 100.
        :type limit: int, optional
        :return: A dictionary containing the activities of the collection.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/collections/{symbol}/activities?offset={offset}&limit={limit}'
        return _make_request(url)

    def get_collection_stats(self, symbol):
        """
        Retrieves stats of a collection by symbol.

        :param symbol: The symbol of the collection to retrieve stats for.
        :type symbol: str
        :return: A dictionary containing the stats of the collection.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/collections/{symbol}/stats'
        return _make_request(url)