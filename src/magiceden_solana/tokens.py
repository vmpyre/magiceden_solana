from helpers.utility import _make_request
from config.endpoints import MAINNET_BASE_URL

class Tokens:
    def __init__(self):
        """
        Initialize the Tokens class.

        :param base_url: The base url for the API endpoint
        :type base_url: str
        """
        self.base_url = MAINNET_BASE_URL
        
    def get_token_metadata(self, mint_address):
        """
        Retrieves metadata for a token/NFT by mint address.

        :param mint_address: The mint address of the token/NFT to retrieve metadata for.
        :type mint_address: str
        :return: A dictionary containing the metadata for the token/NFT.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/tokens/{mint_address}'
        return _make_request(url)

    
    def get_token_listings(self, mint_address):
        """
        Retrieves listings for a token/NFT by mint address.

        :param mint_address: The mint address of the token/NFT to retrieve listings for.
        :type mint_address: str
        :return: A dictionary containing the listings for the token/NFT.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/tokens/{mint_address}/listings'
        return _make_request(url)

    def get_received_offers(self, mint_address, offset=0, limit=100):
        """
        Retrieves received offers for a token/NFT by mint address.

        :param mint_address: The mint address of the token/NFT to retrieve received offers for.
        :type mint_address: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 100.
        :type limit: int, optional
        :return: A dictionary containing the received offers for the token/NFT.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/tokens/{mint_address}/offers_received?offset={offset}&limit={limit}'
        return _make_request(url)
            
    def get_token_activities(self, mint_address, offset=0, limit=100):
        """
        Retrieves activities for a token/NFT by mint address.

        :param mint_address: The mint address of the token/NFT to retrieve activities for.
        :type mint_address: str
        :param offset: The offset for pagination, defaults to 0.
        :type offset: int, optional
        :param limit: The limit for pagination, defaults to 100.
        :type limit: int, optional
        :return: A dictionary containing the activities for the token/NFT.
        :rtype: dict
        :raises ValueError: If the request is not successful, it raises an error with the status code.

        """
        url = f'{self.base_url}/tokens/{mint_address}/activities?offset={offset}&limit={limit}'
        return _make_request(url)
