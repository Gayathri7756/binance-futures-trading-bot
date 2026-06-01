import os
import logging

# Ensure logs directory exists safely
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("trading_bot")