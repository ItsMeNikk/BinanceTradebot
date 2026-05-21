import os
from binance.client import Client


def init_client(api_key=None, api_secret=None):
    if api_key is None:
        api_key = os.getenv("BINANCE_API_KEY")
    if api_secret is None:
        api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("Set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file.")

    use_testnet = os.getenv("BINANCE_USE_TESTNET", "true").lower() == "true"
    return Client(api_key, api_secret, testnet=use_testnet)


def close_client(client):
    pass