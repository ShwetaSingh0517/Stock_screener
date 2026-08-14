import random


def get_stock_data(symbol):

    # Temporary live data simulation

    stock = {

        "symbol": symbol,

        "ltp": random.randint(30,500),

        "bid_qty": random.randint(1000000,5000000),

        "ask_qty": random.randint(1000000,5000000)

    }


    return stock



# Testing

data = get_stock_data("NSE:RELIANCE")


print(data)
