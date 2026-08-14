def calculate_smma(prices, period):

    smma = []

    for i, price in enumerate(prices):

        # First value
        if i == 0:
            smma.append(price)

        else:
            previous = smma[-1]

            value = (
                (previous * (period - 1)) + price
            ) / period

            smma.append(round(value, 2))


    return smma



def generate_signal(smma20, smma120):

    if smma20[-1] > smma120[-1]:

        return "BUY"

    elif smma20[-1] < smma120[-1]:

        return "SELL"

    else:

        return "HOLD"



# Testing

prices = [
    100,
    102,
    105,
    110,
    115,
    120
]


smma_20 = calculate_smma(
    prices,
    20
)


smma_120 = calculate_smma(
    prices,
    120
)


print("SMMA 20:")
print(smma_20)


print("SMMA 120:")
print(smma_120)



signal = generate_signal(
    smma_20,
    smma_120
)


print("Signal:", signal)
def check_crossover(smma20, smma120):

    previous_short = smma20[-2]
    current_short = smma20[-1]

    previous_long = smma120[-2]
    current_long = smma120[-1]


    if previous_short < previous_long and current_short > current_long:

        return "BUY"


    elif previous_short > previous_long and current_short < current_long:

        return "SELL"


    else:

        return "NO SIGNAL"



crossover_signal = check_crossover(
    smma_20,
    smma_120
)


print("Crossover Signal:", crossover_signal)
