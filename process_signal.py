import sys
from datetime import datetime

def process_signal(body):
    _, body_1 = body.split(" symbol ")
    SYMBOL, body_2 = body_1.split(" last ")

    dirty_price, body_3 = body_2.split(" target ")
    PRICE = float(dirty_price)

    dirty_target, body_4 = body_3.split(" stop ")
    TARGET = float(dirty_target)

    dirty_stop_loss, body_5 = body_4.split(" time ")
    STOP_LOSS = float(dirty_stop_loss)

    dirty_time, type = body_5.split(" bull_type ")
    TIME = datetime.strptime(dirty_time, "%Y-%m-%d %H:%M:%S.%f")
    
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
    
    SUBJECT_MATCH = "Trading Signals"
    
    if SUBJECT_MATCH not in issue_title:
        print("Invalid Issue Title")
        sys.exit(1)
    
    results = process_signal(issue_body)
    
    print(results)
