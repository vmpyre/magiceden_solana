from helpers.utility import _make_request
from config.endpoints import MAINNET_BASE_URL

class Instructions:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def buy(self, buyer, auction_house_address, token_mint, price, buyer_referral=None, expiry=None):
        """
        Make a buy instruction request to the API.

        :param buyer: Address of the buyer.
        :type buyer: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param price: Price of the token.
        :type price: str
        :param buyer_referral: Address of the buyer's referral.
        :type buyer_referral: str
        :param expiry: Unix timestamp for the instruction expiry.
        :type expiry: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """
        url = f"{self.base_url}/instructions/buy"
        params = {
            "buyer": buyer,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "price": price,
            "buyerReferral": buyer_referral,
            "expiry": expiry
        }
        return _make_request(url, self.headers, params)

    def buy_now(self, buyer, seller, auction_house_address, token_mint, token_ata, price, buyer_referral=None, seller_referral=None, buyer_expiry=0, seller_expiry=-1, buyer_creator_royalty_percent=100):
        """
        Make a buy now instruction request to the API.

        :param buyer: Address of the buyer.
        :type buyer: str
        :param seller: Address of the seller.
        :type seller: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param token_ata: Address of the token's ATA.
        :type token_ata: str
        :param price: Price of the token.
        :type price: str
        :param buyer_referral: Address of the buyer's referral.
        :type buyer_referral: str
        :param seller_referral: Address of the seller's referral.
        :type seller_referral: str
        :param buyer_expiry: Unix timestamp for the buyer's instruction expiry.
        :type buyer_expiry: int
        :param seller_expiry: Unix timestamp for the seller's instruction expiry.
        :type seller_expiry: int
        :param buyer_creator_royalty_percent: Royalty percentage for the creator of the token.
        :type buyer_creator_royalty_percent: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """ 
        url = f"{self.base_url}/instructions/buy_now"
        params = {
            "buyer": buyer,
            "seller": seller,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "tokenATA": token_ata,
            "price": price,
            "buyerReferral": buyer_referral,
            "sellerReferral": seller_referral,
            "buyerExpiry": buyer_expiry,
            "sellerExpiry": seller_expiry,
            "buyerCreatorRoyaltyPercent": buyer_creator_royalty_percent
        }
        return _make_request(url, self.headers, params)

    def buy_cancel(self, buyer, auction_house_address, token_mint, price, buyer_referral=None, expiry=None):
        """
        Make a buy cancel instruction request to the API.

        :param buyer: Address of the buyer.
        :type buyer: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param price: Price of the token.
        :type price: str
        :param buyer_referral: Address of the buyer's referral.
        :type buyer_referral: str
        :param expiry: Unix timestamp for the instruction expiry.
        :type expiry: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """
        url = f"{self.base_url}/instructions/buy_cancel"
        params = {
            "buyer": buyer,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "price": price,
            "buyerReferral": buyer_referral,
            "expiry": expiry
        }
        return _make_request(url, self.headers, params)

    def buy_change_price(self, buyer, auction_house_address, token_mint, price, new_price, buyer_referral=None, expiry=None):
        """
        Make a buy change price instruction request to the API.

        :param buyer: Address of the buyer.
        :type buyer: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param price: Original price of the token.
        :type price: str
        :param new_price: New price of the token.
        :type new_price: str
        :param buyer_referral: Address of the buyer's referral.
        :type buyer_referral: str
        :param expiry: Unix timestamp for the instruction expiry.
        :type expiry: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """
        url = f"{self.base_url}/instructions/buy_change_price"
        params = {
            "buyer": buyer,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "price": price,
            "newPrice": new_price,
            "buyerReferral": buyer_referral,
            "expiry": expiry
        }
        return _make_request(url, self.headers, params)

    def sell(self, seller, auction_house_address, token_mint, token_account, price, seller_referral=None, expiry=None):
        """
        Make a sell instruction request to the API.

        :param seller: Address of the seller.
        :type seller: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param token_account: Address of the token account.
        :type token_account: str
        :param price: Price of the token.
        :type price: str
        :param seller_referral: Address of the seller's referral.
        :type seller_referral: str
        :param expiry: Unix timestamp for the instruction expiry.
        :type expiry: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """
        url = f"{self.base_url}/instructions/sell"
        params = {
            "seller": seller,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "tokenAccount": token_account,
            "price": price,
            "sellerReferral": seller_referral,
            "expiry": expiry
        }
        return _make_request(url, self.headers, params)

    def sell_now(self, buyer, seller, auction_house_address, token_mint, token_ata, price, new_price, buyer_referral=None, seller_referral=None, buyer_expiry=None, seller_expiry=None):
        """
        Make a sell now instruction request to the API.

        :param buyer: Address of the buyer.
        :type buyer: str
        :param seller: Address of the seller.
        :type seller: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param token_ata: Address of the token ata.
        :type token_ata: str
        :param price: Price of the token.
        :type price: str
        :param new_price: New price of the token.
        :type new_price: str
        :param buyer_referral: Address of the buyer's referral.
        :type buyer_referral: str
        :param seller_referral: Address of the seller's referral.
        :type seller_referral: str
        :param buyer_expiry: Unix timestamp for the buyer instruction expiry.
        :type buyer_expiry: int
        :param seller_expiry: Unix timestamp for the seller instruction expiry.
        :type seller_expiry: int
        :param buyer_creator_royalty_percent: Percentage of the sale that goes to the creator of the token.
        :type buyer_creator_royalty_percent: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """
        url = f"{self.base_url}/instructions/sell_now"
        params = {
            "buyer": buyer,
            "seller": seller,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "tokenATA": token_ata,
            "price": price,
            "newPrice": new_price,
            "buyerReferral": buyer_referral,
            "sellerReferral": seller_referral,
            "buyerExpiry": buyer_expiry,
            "sellerExpiry": seller_expiry
        }
        return _make_request(url, self.headers, params)

    def sell_cancel(self, seller, auction_house_address, token_mint, token_account, price, seller_referral=None, expiry=None):
        """
        Make a sell cancel instruction request to the API.

        :param seller: Address of the seller.
        :type seller: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param token_account: Address of the token account.
        :type token_account: str
        :param price: Price of the token.
        :type price: str
        :param seller_referral: Address of the seller's referral.
        :type seller_referral: str
        :param expiry: Unix timestamp for the instruction expiry.
        :type expiry: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """
        url = f"{self.base_url}/instructions/sell_cancel"
        params = {
            "seller": seller,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "tokenAccount": token_account,
            "price": price,
            "sellerReferral": seller_referral,
            "expiry": expiry
        }
        return _make_request(url, self.headers, params)

    def sell_change_price(self, seller, auction_house_address, token_mint, token_account, price, new_price, seller_referral=None, expiry=None):
        """
        Make a sell change price instruction request to the API.

        :param seller: Address of the seller.
        :type seller: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param token_mint: Address of the token mint.
        :type token_mint: str
        :param token_account: Address of the token account.
        :type token_account: str
        :param price: Original price of the token.
        :type price: str
        :param new_price: New price of the token.
        :type new_price: str
        :param seller_referral: Address of the seller's referral.
        :type seller_referral: str
        :param expiry: Unix timestamp for the instruction expiry.
        :type expiry: int
        :return: API response containing the result of the instruction.
        :rtype: dict
        
        """
        url = f"{self.base_url}/instructions/sell_change_price"
        params = {
            "seller": seller,
            "auctionHouseAddress": auction_house_address,
            "tokenMint": token_mint,
            "tokenAccount": token_account,
            "price": price,
            "newPrice": new_price,
            "sellerReferral": seller_referral,
            "expiry": expiry
        }
        return _make_request(url, self.headers, params)

    def deposit(self, buyer, auction_house_address, amount):
        """
        Make a deposit instruction request to the API.

        :param buyer: Address of the buyer.
        :type buyer: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param amount: Amount to deposit.
        :type amount: int
        :return: API response containing the result of the instruction.
        :rtype: dict

        """
        url = f"{self.base_url}/instructions/deposit"
        params = {
            "buyer": buyer,
            "auctionHouseAddress": auction_house_address,
            "amount": amount
        }
        return _make_request(url, self.headers, params)

    def withdraw(self, buyer, auction_house_address, amount):
        """
        Make a withdraw instruction request to the API.

        :param buyer: Address of the buyer.
        :type buyer: str
        :param auction_house_address: Address of the auction house.
        :type auction_house_address: str
        :param amount: Amount to withdraw.
        :type amount: int
        :return: API response containing the result of the instruction.
        :rtype: dict
        
        """
        url = f"{self.base_url}/instructions/withdraw"
        params = {
            "buyer": buyer,
            "auctionHouseAddress": auction_house_address,
            "amount": amount
        }
        return _make_request(url, self.headers, params)
