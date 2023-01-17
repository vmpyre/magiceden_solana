from helpers.utility import _make_request
from config.endpoints import MAINNET_BASE_URL

class Wallets:
    def __init__(self):
        self.base_url = MAINNET_BASE_URL

    def get_tokens_owned_by_wallet(self, wallet_address, offset=0, limit=100,listStatus='both'):
        """
        Retrieves tokens owned by a wallet by wallet address.

        :param wallet_address: The address of the wallet to retrieve tokens for.
        :type wallet_address: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 100.
        :type limit: int, optional
        :param listStatus: The status of the token, defaults to 'both'.
        :type listStatus: str, optional
        :return: A dictionary containing the tokens owned by the wallet.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/wallets/{wallet_address}/tokens?offset={offset}&limit={limit}&listStatus={listStatus}'
        return _make_request(url)

    def get_wallet_activities(self, wallet_address, offset=0, limit=100):
        """
        Retrieves activities of a wallet by wallet address.

        :param wallet_address: The address of the wallet to retrieve activities for.
        :type wallet_address: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 100.
        :type limit: int, optional
        :return: A dictionary containing the activities of the wallet.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/wallets/{wallet_address}/activities?offset={offset}&limit={limit}'
        return _make_request(url)

    def get_offers_made_by_wallet(self, wallet_address, offset=0, limit=100):
        """
        Retrieves offers made by a wallet by wallet address.

        :param wallet_address: The address of the wallet to retrieve offers for.
        :type wallet_address: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 100.
        :type limit: int, optional
        :return: A dictionary containing the offers made by the wallet.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/wallets/{wallet_address}/offers_made?offset={offset}&limit={limit}'
        return _make_request(url)

    def get_offers_received_by_wallet(self, wallet_address, offset=0, limit=100):
        """
        Retrieves offers received by a wallet by wallet address.

        :param wallet_address: The address of the wallet to retrieve offers for.
        :type wallet_address: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 100.
        :type limit: int, optional
        :return: A dictionary containing the offers received by the wallet.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/wallets/{wallet_address}/offers_received?offset={offset}&limit={limit}'
        return _make_request(url)

    def get_escrow_balance_for_wallet(self, wallet_address):
        """
        Retrieves escrow balance for a wallet by wallet address.

        :param wallet_address: The address of the wallet to retrieve escrow balance for.
        :type wallet_address: str
        :return: A dictionary containing the escrow balance for the wallet.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/wallets/{wallet_address}/escrow_balance'
        return _make_request(url)

    def get_wallet_by_address(self, wallet_address):
        """
        Retrieves a wallet by address.

        :param wallet_address: The address of the wallet to retrieve.
        :type wallet_address: str
        :return: A dictionary containing the wallet information.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/wallets/{wallet_address}'
        return _make_request(url)