import joblib
import pandas as pd


# Load trained model

model = joblib.load(
    "ml/stock_model.pkl"
)


# Current stock price

current_price = 1500


# Create input

data = pd.DataFrame(
    {
        "Close": [current_price]
    }
)


# Prediction

prediction = model.predict(data)


if prediction[0] == 1:

    print("AI Prediction: UP 📈")

else:

    print("AI Prediction: DOWN 📉")
