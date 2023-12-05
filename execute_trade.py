import alpaca_trade_api as tradeapi
import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

ALPACA_KEY = os.getenv("ALPACA_KEY")
ALPACA_SECRET = os.getenv("ALPACA_SECRET")


api = tradeapi.REST(ALPACA_KEY, ALPACA_SECRET,
                    base_url='https://paper-api.alpaca.markets')

# Function to process the trading signal


def execute_trade(signal):
    symbol = signal['symbol']
    price = round(signal['price'], 2)
    target = round(signal['target'], 2)
    stop_loss = round(signal['stop_loss'], 2)
    trade_type = signal['type']  # Assuming 1 for buy and 2 for sell

    # Convert datetime to string for order
    time_str = signal['time'].strftime('%Y-%m-%d %H:%M:%S')

    side = "buy"

    # Place an order
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=1,  # Define quantity as per your requirement
            side=side,
            type='limit',
            time_in_force='gtc',
            limit_price=str(price),
            order_class='bracket',
            take_profit=dict(limit_price=str(target)),
            stop_loss=dict(stop_price=str(stop_loss))
        )
        return order
    except Exception as e:
        return str(e)


test_signal = {
    'symbol': 'IDXX',
    'price': 466.66,
    'target': 473.5780678996626,
    'stop_loss': 460.2381932100337,
    'time': datetime.datetime(2023, 12, 1, 14, 34, 55, 449134),
    'type': 2
}
