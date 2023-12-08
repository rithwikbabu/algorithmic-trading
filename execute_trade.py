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

# Define the proportions for each position
POSITION_SIZES = [.2, .2, .2, .2, .2]


def execute_trade(signal):
    symbol = signal['symbol']
    price = round(signal['price'], 2)
    target = round(signal['target'], 2)
    stop_loss = round(signal['stop_loss'], 2)

    # Get account information
    account = api.get_account()
    account_balance = float(account.equity)

    # Calculate the value for each position based on the current account balance
    position_values = [size * account_balance for size in POSITION_SIZES]

    # Get a list of current positions
    positions = api.list_positions()

    # Determine the next available position size
    if len(positions) < len(POSITION_SIZES):
        next_position_size = position_values[len(positions)]
    else:
        return "Maximum positions reached"

    # Calculate the number of shares to buy for the next position
    qty = int(next_position_size / price)

    side = "buy"

    # Place an order
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=int(qty),  # Updated quantity based on position size
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

# Example usage
# signal = {'symbol': 'AAPL', 'price': 150, 'target': 160, 'stop_loss': 145, 'time': datetime.datetime.now()}
# execute_trade(signal)
