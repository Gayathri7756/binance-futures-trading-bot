def validate_order_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Validates CLI inputs before touching the real Binance API network.
    """
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a valid string string (e.g., BTCUSDT).")

    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("side must be BUY or SELL")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("quantity must be greater than 0")

    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        raise ValueError("price required and must be greater than 0 for LIMIT orders")