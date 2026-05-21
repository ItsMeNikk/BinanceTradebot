# binancetradebot

A simple Binance Futures Testnet trading bot built with Python.

> Educational project — do not use with real funds.

## Features

- MARKET and LIMIT orders
- BUY and SELL support
- Interactive CLI mode
- Direct CLI commands
- Order status checking
- Order cancellation
- Account and balance info
- Input validation
- Logging and error handling

## Screenshot

![Trading Bot Screenshot](screenshots/Tradebot.png)

## Requirements

- Python 3.9+
- Binance Futures Testnet account
- Binance Testnet API keys

## Setup

### Clone Repository

```bash
git clone https://github.com/ItsMeNikk/BinanceTradebot.git
cd BinanceTradebot
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

#### Windows

```bash
copy .env.example .env
```

#### macOS/Linux

```bash
cp .env.example .env
```

Add your Binance Testnet API keys inside `.env`:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

## Binance Futures Testnet

https://testnet.binancefuture.com

## Run Application

### Interactive Mode

```bash
python cli.py
```

### MARKET Order

```bash
python cli.py market BTCUSDT BUY 0.01
```

### LIMIT Order

```bash
python cli.py limit BTCUSDT SELL 0.05 50000
```

### Check Order Status

```bash
python cli.py status BTCUSDT 12345678
```

### Cancel Order

```bash
python cli.py cancel BTCUSDT 12345678
```

### Account Information

```bash
python cli.py account
```

### Balance Information

```bash
python cli.py balance
```

## Logging

Logs are stored in:

```text
logs/trading_bot.log
```

## Technologies Used

- Python
- python-binance
- argparse
- logging
- python-dotenv

## Disclaimer

This project is for educational and assessment purposes only.

## Author

Nikhil

GitHub: https://github.com/ItsMeNikk
