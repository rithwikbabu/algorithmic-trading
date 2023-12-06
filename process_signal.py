import sys
from datetime import datetime

from execute_trade import execute_trade

def process_signal(body):
    body_0 = body.replace('\n', ' ')
    _, body_1 = body_0.strip().split("symbol")
    
    dirty_symbol, body_2 = body_1.strip().split("last")
    SYMBOL = dirty_symbol.strip()

    dirty_price, body_3 = body_2.strip().split("target")
    PRICE = float(dirty_price.strip())

    dirty_target, body_4 = body_3.strip().split("stop")
    TARGET = float(dirty_target.strip())

    dirty_stop_loss, body_5 = body_4.strip().split("time")
    STOP_LOSS = float(dirty_stop_loss.strip())

    dirty_time, type = body_5.strip().split("bull_type")
    TIME = datetime.strptime(dirty_time.strip(), "%Y-%m-%d %H:%M:%S.%f")
    
    TYPE = int(type.strip())
    
    trade_data = {
        "symbol": SYMBOL,
        "price": PRICE,
        "target": TARGET,
        "stop_loss": STOP_LOSS,
        "time": TIME,
        "type": TYPE
    }
    
    return trade_data

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_signal.py [title] [body]")
        sys.exit(1)

    issue_title = sys.argv[1]
    issue_body = sys.argv[2]
    
    SUBJECT_MATCH = "Trading signals"
    
    if SUBJECT_MATCH not in issue_title:
        print("Invalid Issue Title")
        sys.exit(1)
    
    signal_data = process_signal(issue_body)
    
    print(signal_data)
    
    print("Trading...")
    
    try:
        response = execute_trade(signal_data)
        print("Order placed!")

        print(response)
    except Exception as e:
        print("Order failed! ", e)
