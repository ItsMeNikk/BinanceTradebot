import argparse
from pathlib import Path

from dotenv import load_dotenv
from bot.logging_config import setup_logging

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

setup_logging()


def fmt_money(val):
    try:
        return f"{float(val):,.2f}"
    except (ValueError, TypeError):
        return val


def show_order(order):
    print(f"\n  Order ID    : {order.get('orderId', '?')}")
    print(f"  Symbol     : {order.get('symbol', '?')}")
    print(f"  Side       : {order.get('side', '?')}")
    print(f"  Type       : {order.get('type', '?')}")
    print(f"  Price      : {order.get('price', '?')}")
    print(f"  Qty        : {order.get('origQty', '?')}")
    print(f"  Filled     : {order.get('executedQty', '?')}")
    print(f"  Status     : {order.get('status', '?')}")
    print()


def show_account():
    from bot.orders import get_account_info
    try:
        acc = get_account_info()
    except Exception as e:
        print(f"\n  Error: {e}\n")
        return

    assets = acc.get("assets", [])
    print("\n  === Account ===")
    print(f"  Wallet Balance : {fmt_money(acc.get('totalWalletBalance', '0'))} USDT")
    print(f"  Available      : {fmt_money(acc.get('availableBalance', '0'))} USDT")
    print(f"  Unrealized PnL : {fmt_money(acc.get('totalUnrealizedProfit', '0'))} USDT")
    print(f"  Margin Balance : {fmt_money(acc.get('totalMarginBalance', '0'))} USDT")
    print()

    if assets:
        print("  --- Assets ---")
        for a in assets:
            if float(a.get("walletBalance", 0)) != 0 or float(a.get("unrealizedProfit", 0)) != 0:
                bal = fmt_money(a.get("walletBalance", "0"))
                pnl = fmt_money(a.get("unrealizedProfit", "0"))
                print(f"  {a['asset']:<8}  Balance: {bal:>12}  PnL: {pnl:>12}")
        print()


def show_balance():
    from bot.orders import get_account_info
    try:
        acc = get_account_info()
        print(f"\n  Balance    : {fmt_money(acc.get('availableBalance', '0'))} USDT")
        print(f"  Total      : {fmt_money(acc.get('totalWalletBalance', '0'))} USDT")
        print(f"  Unrealized : {fmt_money(acc.get('totalUnrealizedProfit', '0'))} USDT\n")
    except Exception as e:
        print(f"\n  Error: {e}\n")


def place_market_order_cli(symbol, side, quantity):
    from bot.orders import place_market_order
    try:
        order = place_market_order(symbol, side, quantity)
        print(f"\n  Order placed! ID: {order.get('orderId', '?')}  Status: {order.get('status', '?')}\n")
    except Exception as e:
        print(f"\n  Error: {e}\n")


def place_limit_order_cli(symbol, side, quantity, price):
    from bot.orders import place_limit_order
    try:
        order = place_limit_order(symbol, side, quantity, price)
        print(f"\n  Order placed! ID: {order.get('orderId', '?')}  Status: {order.get('status', '?')}\n")
    except Exception as e:
        print(f"\n  Error: {e}\n")


def check_order_cli(symbol, order_id):
    from bot.orders import get_order_status
    try:
        show_order(get_order_status(order_id, symbol))
    except Exception as e:
        print(f"\n  Error: {e}\n")


def cancel_order_cli(symbol, order_id):
    from bot.orders import cancel_order
    try:
        cancel_order(order_id, symbol)
        print(f"\n  Order {order_id} cancelled on {symbol}.\n")
    except Exception as e:
        print(f"\n  Error: {e}\n")


def menu_loop():
    from bot.validators import validate_symbol, validate_symbol_exists, validate_side

    print()
    print("  ==================================")
    print("    Binance Futures Testnet Bot")
    print("  ==================================")

    while True:
        print()
        print("  1 - Account Info")
        print("  2 - Balance")
        print("  3 - Market Order")
        print("  4 - Limit Order")
        print("  5 - Check Order")
        print("  6 - Cancel Order")
        print("  0 - Exit")
        print()

        choice = input("  Choice: ").strip()

        if choice == "1":
            show_account()
        elif choice == "2":
            show_balance()
        elif choice == "3":
            from bot.orders import place_market_order
            symbol = input("  Symbol (e.g. BTCUSDT): ").strip().upper()
            try:
                validate_symbol(symbol)
                validate_symbol_exists(symbol)
            except ValueError as err:
                print(f"  Error: {err}\n")
                continue
            side = input("  Side (BUY/SELL): ").strip().upper()
            if side not in ("BUY", "SELL"):
                print("  Side must be BUY or SELL.\n")
                continue
            qty = input("  Quantity: ").strip()
            try:
                qty = float(qty)
            except ValueError:
                print("  Quantity must be a number.\n")
                continue
            place_market_order_cli(symbol, side, qty)

        elif choice == "4":
            from bot.orders import place_limit_order
            symbol = input("  Symbol (e.g. BTCUSDT): ").strip().upper()
            try:
                validate_symbol(symbol)
                validate_symbol_exists(symbol)
            except ValueError as err:
                print(f"  Error: {err}\n")
                continue
            side = input("  Side (BUY/SELL): ").strip().upper()
            if side not in ("BUY", "SELL"):
                print("  Side must be BUY or SELL.\n")
                continue
            qty = input("  Quantity: ").strip()
            try:
                qty = float(qty)
            except ValueError:
                print("  Quantity must be a number.\n")
                continue
            price = input("  Price: ").strip()
            try:
                price = float(price)
            except ValueError:
                print("  Price must be a number.\n")
                continue
            place_limit_order_cli(symbol, side, qty, price)

        elif choice == "5":
            symbol = input("  Symbol (e.g. BTCUSDT): ").strip().upper()
            try:
                validate_symbol(symbol)
                validate_symbol_exists(symbol)
            except ValueError as err:
                print(f"  Error: {err}\n")
                continue
            oid = input("  Order ID: ").strip()
            try:
                oid = int(oid)
            except ValueError:
                print("  Order ID must be a number.\n")
                continue
            check_order_cli(symbol, oid)

        elif choice == "6":
            symbol = input("  Symbol (e.g. BTCUSDT): ").strip().upper()
            try:
                validate_symbol(symbol)
                validate_symbol_exists(symbol)
            except ValueError as err:
                print(f"  Error: {err}\n")
                continue
            oid = input("  Order ID: ").strip()
            try:
                oid = int(oid)
            except ValueError:
                print("  Order ID must be a number.\n")
                continue
            cancel_order_cli(symbol, oid)

        elif choice == "0":
            print("\n  Bye!\n")
            break
        else:
            print("  Unknown option, pick 0-6.\n")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("account", help="Show account info")
    sub.add_parser("balance", help="Show balance")

    m = sub.add_parser("market", help="Place market order")
    m.add_argument("symbol")
    m.add_argument("side")
    m.add_argument("quantity", type=float)

    l = sub.add_parser("limit", help="Place limit order")
    l.add_argument("symbol")
    l.add_argument("side")
    l.add_argument("quantity", type=float)
    l.add_argument("price", type=float)

    s = sub.add_parser("status", help="Check order status")
    s.add_argument("symbol")
    s.add_argument("order_id", type=int)

    c = sub.add_parser("cancel", help="Cancel order")
    c.add_argument("symbol")
    c.add_argument("order_id", type=int)

    args = parser.parse_args()

    if args.command == "account":
        show_account()
    elif args.command == "balance":
        show_balance()
    elif args.command == "market":
        place_market_order_cli(args.symbol.upper(), args.side.upper(), args.quantity)
    elif args.command == "limit":
        place_limit_order_cli(args.symbol.upper(), args.side.upper(), args.quantity, args.price)
    elif args.command == "status":
        check_order_cli(args.symbol.upper(), args.order_id)
    elif args.command == "cancel":
        cancel_order_cli(args.symbol.upper(), args.order_id)
    else:
        menu_loop()


if __name__ == "__main__":
    main()