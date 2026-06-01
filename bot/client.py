import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_futures_client() -> Client:
    """
    Initializes and returns a Binance Client explicitly locked onto the Futures Testnet.
    """
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API Keys are missing from your configuration. Please check your .env file.")

    # Initialize client explicitly pointing to the test network
    client = Client(api_key, api_secret, testnet=True)
    return client