# magiceden_solana

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

Then, create instances of the classes to interact with the corresponding API endpoints:
```python
tokens_api = Tokens()
```

For example, you can use the get_token_metadata() method of the Tokens class to retrieve metadata of a token by its mint address:
```python
tokens_api.get_token_metadata("127icS59959eL776pCWKTUAoWqk8voexAzAs9wiAHfEx")
```
The SDK also provides additional functionality for interacting with the Wallets, Collections and Launchpad endpoints of the Magiceden API.
You can find more details in the documentation.

## Contribution
Feel free to open issues, pull requests and submit feedback. We appreciate your help!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to the Magiceden team for providing the API Key.

## Disclaimer
This SDK is not affiliated with, endorsed, or sponsored by magiceden. It was created by [vmpyre.sol#0001](https://discordapp.com/users/473884990837489675) (Discord) for personal use and is now being made open-source for others to use and contribute to. The developer of this SDK is not responsible for any errors or issues that may occur when using this SDK. Use at your own risk.

