import re
import logging

logger = logging.getLogger(__name__)

_cache = {}


def _fetch_symbols():
    if _cache.get("symbols"):
        return _cache["symbols"]

    from bot.client import init_client
    client = init_client()
    info = client.futures_exchange_info()
    _cache["symbols"] = {s["symbol"] for s in info.get("symbols", [])}
    logger.debug(f"Loaded {len(_cache['symbols'])} pairs from Binance")
    return _cache["symbols"]


def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    symbol = symbol.upper().strip()

    if not re.match(r"^[A-Z]{2,10}$", symbol):
        raise ValueError(f"'{symbol}' doesn't look like a valid symbol.")

    return symbol


def validate_symbol_exists(symbol):
    symbols = _fetch_symbols()
    if symbol not in symbols:
        raise ValueError(f"'{symbol}' pair not available.")
    return symbol


def validate_quantity(quantity):
    if quantity is None or quantity <= 0:
        raise ValueError(f"Quantity must be greater than zero, got: {quantity}")
    return quantity


def validate_price(price):
    if price is None or price <= 0:
        raise ValueError(f"Price must be greater than zero, got: {price}")
    return price


def validate_side(side):
    side = side.upper().strip()
    if side not in ("BUY", "SELL"):
        raise ValueError(f"Side must be BUY or SELL, got: {side}")
    return side