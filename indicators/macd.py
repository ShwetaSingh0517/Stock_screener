def calculate_ema(prices, period):

    ema = []

    multiplier = 2 / (period + 1)

    for i, price in enumerate(prices):

        if i == 0:

            ema.append(price)

        else:

            value = (
                (price - ema[-1]) * multiplier
            ) + ema[-1]

            ema.append(round(value, 2))


    return ema



def calculate_macd(prices):

    ema12 = calculate_ema(
        prices,
        12
    )


    ema26 = calculate_ema(
        prices,
        26
    )


    macd_line = []


    for i in range(len(prices)):

        value = ema12[i] - ema26[i]

        macd_line.append(
            round(value, 2)
        )


    return macd_line



def macd_signal(macd):

    if macd[-1] > macd[-2]:

        return "BUY"

    elif macd[-1] < macd[-2]:

        return "SELL"

    else:

        return "HOLD"
