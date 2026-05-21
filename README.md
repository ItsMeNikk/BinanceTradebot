# binancetradebot

A simple Binance Futures Testnet trading bot CLI in Python.

> For educational use only. Do not use with real funds.

## Setup

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
cp .env.example .env            # then add your testnet API keys
```

## Run

```bash
python cli.py --help
```

## Commands

```bash
python cli.py market --symbol BTCUSDT --side BUY --quantity 0.01
python cli.py limit  --symbol BTCUSDT --side SELL --quantity 0.05 --price 50000
python cli.py status --symbol BTCUSDT --order-id 12345678
python cli.py cancel --symbol BTCUSDT --order-id 12345678
python cli.py account
```
Logs are saved to `logs/trading_bot.log`.
