import logging

from bot.validators import validate_symbol, validate_symbol_exists, validate_quantity, validate_price, validate_side

logger = logging.getLogger(__name__)

_client = None


def _get_client():
    global _client
    if _client is None:
        from bot.client import init_client
        _client = init_client()
    return _client


def _get_price(symbol):
    try:
        client = _get_client()
        ticker = client.futures_ticker(symbol=symbol)
        return ticker.get("lastPrice", "N/A")
    except Exception:
        return "N/A"


def place_market_order(symbol, side, quantity):
    symbol = validate_symbol(symbol)
    validate_symbol_exists(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)

    price = _get_price(symbol)

    logger.info(f"MARKET {side} {quantity} {symbol} @ market price")

    client = _get_client()
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
    )

    order_id = order.get("orderId")
    status = order.get("status")
    logger.info(f"Order placed  |  ID: {order_id}  |  Status: {status}  |  Qty: {quantity}  |  Price: {price}  |  {side}  |  {symbol}")
    return order


def place_limit_order(symbol, side, quantity, price):
    symbol = validate_symbol(symbol)
    validate_symbol_exists(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)
    price = validate_price(price)

    current_price = _get_price(symbol)

    logger.info(f"LIMIT {side} {quantity} {symbol} @ {price}")

    client = _get_client()
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price,
    )

    order_id = order.get("orderId")
    status = order.get("status")
    logger.info(f"Order placed  |  ID: {order_id}  |  Status: {status}  |  Qty: {quantity}  |  Limit Price: {price}  |  Current: {current_price}  |  {side}  |  {symbol}")
    return order


def get_order_status(order_id, symbol):
    symbol = validate_symbol(symbol)

    logger.info(f"Checking order  |  ID: {order_id}  |  {symbol}")

    client = _get_client()
    order = client.futures_get_order(symbol=symbol, orderId=order_id)

    logger.info(f"Order status  |  ID: {order_id}  |  Status: {order.get('status')}  |  Filled: {order.get('executedQty')}/{order.get('origQty')}  |  Avg Price: {order.get('avgPrice')}  |  {symbol}")
    return order


def cancel_order(order_id, symbol):
    symbol = validate_symbol(symbol)

    logger.info(f"Cancelling order  |  ID: {order_id}  |  {symbol}")

    client = _get_client()
    result = client.futures_cancel_order(symbol=symbol, orderId=order_id)

    logger.info(f"Order cancelled  |  ID: {order_id}")
    return result


def get_account_info():
    logger.info("Fetching account info")

    client = _get_client()
    acc = client.futures_account()

    usdt_balance = acc.get("totalWalletBalance", "0")
    available = acc.get("availableBalance", "0")
    unrealized_pnl = acc.get("totalUnrealizedProfit", "0")

    logger.info(f"Account loaded  |  Balance: {usdt_balance} USDT  |  Available: {available} USDT  |  Unrealized PnL: {unrealized_pnl} USDT")
    return acc