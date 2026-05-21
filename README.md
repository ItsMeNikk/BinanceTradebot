binancetradebot

A simple Binance Futures Testnet trading bot CLI in Python.



For educational use only. Do not use with real funds.

Setup

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
cp .env.example .env            # then add your testnet API keys

Run

python cli.py --help

Commands

python cli.py market --symbol BTCUSDT --side BUY --quantity 0.01
python cli.py limit  --symbol BTCUSDT --side SELL --quantity 0.05 --price 50000
python cli.py status --symbol BTCUSDT --order-id 12345678
python cli.py cancel --symbol BTCUSDT --order-id 12345678
python cli.py account

What to implement







File



Functions



Status





bot/client.py



init_client()



Done





bot/orders.py



place_market_order(), place_limit_order(), etc.



Done





bot/validators.py



validate_quantity(), validate_price()



Done

Logs are saved to logs/trading_bot.log.
