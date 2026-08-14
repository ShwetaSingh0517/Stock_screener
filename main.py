import pandas as pd

from indicators.smma import calculate_smma, generate_signal
from Stock_screener import filter_stocks


# -------------------------
# Read Stock CSV Data
# -------------------------

data = pd.read_csv("data/stock_data.csv")


print("Stock Data Loaded")
print(data)


# -------------------------
# Convert CSV Data to Stock Format
# -------------------------

stocks = []


for index, row in data.iterrows():

    stock = {

        "symbol": row["Symbol"],

        "ltp": row["Close"],

        "bid_qty": 2000000,

        "ask_qty": 2000000

    }

    stocks.append(stock)



# -------------------------
# Stock Filtering
# -------------------------

selected = filter_stocks(stocks)



print("\nSelected Stocks")
print("----------------")


for stock in selected:

    print(stock)



# -------------------------
# SMMA Calculation
# -------------------------

prices = data["Close"].tolist()



smma_20 = calculate_smma(
    prices,
    20
)


smma_120 = calculate_smma(
    prices,
    120
)



print("\nSMMA 20")
print(smma_20)


print("\nSMMA 120")
print(smma_120)



# -------------------------
# Trading Signal
# -------------------------

signal = generate_signal(
    smma_20,
    smma_120
)


print("\nFinal Trading Signal:")
print(signal)
