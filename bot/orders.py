import json
from binance.exceptions import BinanceAPIException
from requests.exceptions import ConnectionError, Timeout
from bot.logging_config import logger
from bot.client import get_futures_client

def place_futures_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Sends execution request to Binance Futures Testnet and structures audit logs.
    """
    try:
        client = get_futures_client()
        
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        # Build clean JSON format structure for request logs
        request_log = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }
        if price:
            request_log["price"] = price
            
        logger.info(f"Request:\n{json.dumps(request_log, indent=1)}")

        # Execute API endpoints based on order variant types
        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=str(price),
                timeInForce="GTC"  # Good 'Til Cancelled is standard required for Limit orders
            )
        else:
            raise ValueError(f"Unsupported order type: {order_type}")

        # Log response string data received from server
        logger.info(f"Response:\n{json.dumps(response, indent=1)}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e.message} (Code: {e.code})")
        raise RuntimeError(f"Binance API Error: {e.message}")
    except (ConnectionError, Timeout) as e:
        logger.error(f"Network Connection Issue: {str(e)}")
        raise RuntimeError("Network Error: Verification failed. Server unreachable.")