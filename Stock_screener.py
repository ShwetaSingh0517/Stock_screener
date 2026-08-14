def filter_stocks(stock_data):

    selected_stocks = []


    for stock in stock_data:

        ltp = stock["ltp"]
        bid_qty = stock["bid_qty"]
        ask_qty = stock["ask_qty"]


        # Price Condition

        if 30 <= ltp <= 500:


            # Liquidity Condition

            if bid_qty > 1000000 and ask_qty > 1000000:

                selected_stocks.append(stock)


    return selected_stocks



# Sample Stock Data

stocks = [

    {
        "symbol": "ABC",
        "ltp": 120,
        "bid_qty": 1500000,
        "ask_qty": 2000000
    },


    {
        "symbol": "XYZ",
        "ltp": 700,
        "bid_qty": 3000000,
        "ask_qty": 2500000
    },


    {
        "symbol": "PQR",
        "ltp": 250,
        "bid_qty": 1200000,
        "ask_qty": 1500000
    }

]



result = filter_stocks(stocks)



print("Eligible Stocks")


for stock in result:

    print(
        stock["symbol"],
        stock["ltp"]
    )