import argparse
import sys
from bot.validators import validate_order_inputs
from bot.orders import place_futures_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading CLI Bot")
    
    parser.add_argument("--symbol", type=str, required=True, help="Trading Pair (e.g. BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, help="BUY or SELL")
    parser.add_argument("--type", type=str, required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order Asset Quantity")
    parser.add_argument("--price", type=float, default=None, help="Order Price (Required for LIMIT)")

    args = parser.parse_args()

    # 1. Validation check
    try:
        validate_order_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # 2. Display Order Summary Context 
    print("\n===== ORDER SUMMARY =====\n")
    print(f"Symbol: {args.symbol.upper()}")
    print(f"Side: {args.side.upper()}")
    print(f"Type: {args.type.upper()}")
    print(f"Quantity: {args.quantity}")
    if args.price:
        print(f"Price: {args.price}")
    print("\n=========================")

    # 3. Process Live Order Execution
    try:
        print("\nSending order to Binance Futures Testnet...")
        response = place_futures_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        # 4. Success UI Format output processing
        order_id = response.get("orderId")
        status = response.get("status")
        executed_qty = response.get("executedQty", args.quantity)
        avg_price = response.get("avgPrice") or response.get("price", "N/A")

        print("\n===== RESPONSE =====\n")
        print(f"Order ID: {order_id}")
        print(f"Status: {status}")
        print(f"Executed Qty: {executed_qty}")
        print(f"Average Price: {avg_price}")
        print("\nOrder placed successfully.")

    except RuntimeError as e:
        print(f"\nExecution Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()