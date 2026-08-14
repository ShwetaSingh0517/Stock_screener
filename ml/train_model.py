import pandas as pd

from sklearn.ensemble import RandomForestClassifier

import joblib



# Load Data

data = pd.read_csv(
    "data/stock_data.csv"
)



# Create Target

# Future price higher = 1 (UP)
# Future price lower = 0 (DOWN)

data["Target"] = (
    data["Close"].shift(-1) > data["Close"]
).astype(int)



# Remove empty row

data = data.dropna()



# Features

X = data[["Close"]]

y = data["Target"]



# Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)



# Train

model.fit(
    X,
    y
)



# Save Model

joblib.dump(
    model,
    "ml/stock_model.pkl"
)



print("AI Model Training Complete")
