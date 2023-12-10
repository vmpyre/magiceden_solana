# MagicEden APIs Python SDK 

Python SDK for interacting with the [Magiceden Official APIs - https://api.magiceden.dev/](https://api.magiceden.dev/).

## Installation

### Installing Using PIP (Recommended)
```python
pip install magiceden_solana
```

### Installing from Source

1. Clone the repository: git clone https://github.com/vmpyre/magiceden_solana.git

2. Change into the project directory: cd magiceden_solana

3. Install the dependencies: pip install -r requirements.txt

## Usage

First, import the SDK's classes:
```python
from magiceden_solana import Tokens, Wallets, Collections, Launchpad, Instructions
```

Then, create instances of the classes to interact with the corresponding API endpoints (in this case the Tokens class):
```python
tokens_api = Tokens()
```

For example, you can use the get_token_metadata() method of the Tokens class to retrieve metadata of a token by its mint address:
```python
tokens_api.get_token_metadata("TOKEN ADDRESS HERE")
```
The SDK also provides additional functionality for interacting with the Wallets, Collections, Launchpad and Instructions endpoints of the Magiceden API.
You can find details about the class methods below

## Class Methods
See the Official Magiceden documentation for function arguments here: https://api.magiceden.dev/

### Tokens
- get_token_metadata()
- get_token_listings()
- get_received_offers()
- get_token_activities()

### Wallets
- get_tokens_owned_by_wallet()
- get_wallet_activities()
- get_offers_made_by_wallet()
- get_offers_received_by_wallet()
- get_escrow_balance_for_wallet()
- get_wallet_by_address()

### Collections
- get_collections()
- get_collection_listings()
- get_collection_activities()
- get_collection_stats()
- get_collection_holder_stats()

### Launchpad
- get_launchpad_collections()

### Marketplace
- get_top_50_collections()

### Instructions
- buy()
- buy_now()
- buy_cancel()
- buy_change_price()
- sell()
- sell_now()
- sell_cancel()
- sell_change_price()
- deposit()
- withdraw()

## Contribution
Feel free to open issues, pull requests and submit feedback. We appreciate your help!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to the Magiceden team for providing the API Key.

## Disclaimer
This SDK is not affiliated with, endorsed, or sponsored by magiceden. It was created by [vmpyre.sol#0001](https://discordapp.com/users/473884990837489675) (Discord) for personal use and is now being made open-source for others to use and contribute to. The developer of this SDK is not responsible for any errors or issues that may occur when using this SDK. Use at your own risk.

