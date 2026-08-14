def calculate_risk(price, signal):

    if signal == "BUY":

        stop_loss = price * 0.97

        target = price * 1.06


    elif signal == "SELL":

        stop_loss = price * 1.03

        target = price * 0.94


    else:

        stop_loss = price

        target = price



    return (
        round(stop_loss, 2),
        round(target, 2)
    )



def risk_level(price, stop_loss, target):

    risk = abs(price - stop_loss)

    reward = abs(target - price)


    ratio = reward / risk


    if ratio >= 2:

        return "Low Risk"


    elif ratio >= 1:

        return "Medium Risk"


    else:

        return "High Risk"
