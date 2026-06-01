# Binance Futures Testnet Trading Bot CLI

A lightweight, robust command-line interface (CLI) built to interact with the Binance Futures Testnet API.

## Features
- **Market Orders**: Execute trades instantly at the current testnet market price.
- **Limit Orders**: Place advanced trades with user-specified target prices.
- **BUY / SELL support**: Full coverage for entering long or short positions.
- **Input Validation**: Hardened validation layer preventing malformed requests.
- **Logging**: Streamlined historical record-keeping of every execution payload.
- **Error Handling**: Graceful network and API failure handling instead of application crashes.

## Installation & Setup

### 1. Configure Environment & Install Dependencies
```bash
python -m venv venv
# Activate (Windows): venv\Scripts\activate
# Activate (Mac/Linux): source venv/bin/activate

pip install -r requirements.txt