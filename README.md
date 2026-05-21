# binancetradebot

A simple Binance Futures Testnet trading bot in Python.

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

The bot supports two modes: interactive menu and direct CLI commands.

### Interactive Menu

```bash
python cli.py
```

### CLI Commands

```
python cli.py market BTCUSDT BUY 0.01
python cli.py limit  BTCUSDT SELL 0.05 50000
python cli.py status BTCUSDT 12345678
python cli.py cancel BTCUSDT 12345678
python cli.py account
python cli.py balance
```

Run `python cli.py` (no arguments) to launch the interactive menu instead.
