
from helpers.utility import _make_request
from config.endpoints import MAINNET_BASE_URL

class Launchpad:
    def __init__(self):
        self.base_url = MAINNET_BASE_URL

    def get_launchpad_collections(self, offset=0, limit=200):
        """
        Retrieves launchpad collections.

        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 200.
        :type limit: int, optional
        :return: A dictionary containing the launchpad collections.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/launchpad/collections?offset={offset}&limit={limit}'
        return _make_request(url)
