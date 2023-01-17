from helpers.utility import _make_request
from config.endpoints import MAINNET_BASE_URL

class Instructions:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def buy(self, buyer, auction_house_address, token_mint, price, buyer_referral=None, expiry=None):
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
        url = f"{self.base_url}/instructions/deposit"
        params = {
            "buyer": buyer,
            "auctionHouseAddress": auction_house_address,
            "amount": amount
        }
        return _make_request(url, self.headers, params)

    def withdraw(self, buyer, auction_house_address, amount):
        url = f"{self.base_url}/instructions/withdraw"
        params = {
            "buyer": buyer,
            "auctionHouseAddress": auction_house_address,
            "amount": amount
        }
        return _make_request(url, self.headers, params)
