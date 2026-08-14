import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

from indicators.smma import calculate_smma, generate_signal
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd, macd_signal
from trading.risk_management import calculate_risk, risk_level


# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="AI Stock Screener",
    page_icon="📈",
    layout="wide"
)


# =========================
# Custom CSS
# =========================

st.markdown("""
<style>

.main {
    background-color:#0e1117;
}

h1 {
    color:#00ff99;
}

.metric-card {
    background:#161b22;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #30363d;
}

.metric-title {
    color:#8b949e;
    font-size:14px;
}

.metric-value {
    color:white;
    font-size:28px;
    font-weight:bold;
}

.buy {
    color:#00ff99;
    font-size:30px;
    font-weight:bold;
}

.sell {
    color:#ff4b4b;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)



# =========================
# Title
# =========================

st.title("📈 AI Stock Screener Dashboard")

st.caption(
    "SMMA + RSI + MACD + AI Prediction + Risk Management"
)



# =========================
# Load Data
# =========================

data = pd.read_csv(
    "data/stock_data.csv"
)



# =========================
# Sidebar
# =========================

st.sidebar.header("⚙️ Stock Settings")

stocks = data["Symbol"].unique()

selected_stock = st.sidebar.selectbox(
    "Choose Stock",
    stocks
)



stock_data = data[
    data["Symbol"] == selected_stock
]


prices = stock_data["Close"].tolist()



# =========================
# Indicators
# =========================

smma20 = calculate_smma(
    prices,
    20
)

smma120 = calculate_smma(
    prices,
    120
)


smma_signal = generate_signal(
    smma20,
    smma120
)



rsi_value = calculate_rsi(
    prices
)



macd_values = calculate_macd(
    prices
)


macd_result = macd_signal(
    macd_values
)



# =========================
# AI Prediction
# =========================

model = joblib.load(
    "ml/stock_model.pkl"
)


prediction = model.predict(
    pd.DataFrame(
        {
            "Close":[prices[-1]]
        }
    )
)


if prediction[0] == 1:
    ai_prediction = "UP 📈"
else:
    ai_prediction = "DOWN 📉"



# =========================
# Risk
# =========================

entry_price = prices[-1]


stop_loss, target = calculate_risk(
    entry_price,
    smma_signal
)


risk = risk_level(
    entry_price,
    stop_loss,
    target
)
# =========================
# Dashboard Cards
# =========================

st.subheader("📊 Market Overview")


c1, c2, c3, c4, c5, c6 = st.columns(6)


def card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )



with c1:
    card(
        "Stock",
        selected_stock
    )


with c2:
    card(
        "Price",
        f"₹{entry_price}"
    )


with c3:
    card(
        "SMMA",
        smma_signal
    )


with c4:
    card(
        "AI",
        ai_prediction
    )


with c5:
    card(
        "RSI",
        round(rsi_value,2)
    )


with c6:
    card(
        "MACD",
        macd_result
    )



# =========================
# Risk Management
# =========================

st.subheader("🛡️ Risk Management")


r1,r2,r3 = st.columns(3)


with r1:
    card(
        "Entry Price",
        f"₹{entry_price}"
    )


with r2:
    card(
        "Stop Loss",
        f"₹{stop_loss}"
    )


with r3:
    card(
        "Target",
        f"₹{target}"
    )


st.info(
    f"Risk Level : {risk}"
)



# =========================
# Interactive Chart
# =========================

st.subheader("📈 Price & SMMA Trend")


fig = go.Figure()


fig.add_trace(
    go.Scatter(
        y=prices,
        mode="lines",
        name="Price"
    )
)


fig.add_trace(
    go.Scatter(
        y=smma20,
        mode="lines",
        name="SMMA 20"
    )
)


fig.add_trace(
    go.Scatter(
        y=smma120,
        mode="lines",
        name="SMMA 120"
    )
)


fig.update_layout(
    height=450,
    template="plotly_dark"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# =========================
# Final Recommendation
# =========================

st.subheader("🤖 Final Recommendation")


if (
    smma_signal=="BUY"
    and ai_prediction=="UP 📈"
    and macd_result=="BUY"
):

    st.success(
        "🚀 STRONG BUY SIGNAL"
    )


elif (
    smma_signal=="SELL"
    and ai_prediction=="DOWN 📉"
):

    st.error(
        "🔻 STRONG SELL SIGNAL"
    )


else:

    st.warning(
        "⏳ WAIT / HOLD"
    )



# =========================
# Stock History
# =========================

st.subheader("📄 Stock History")

st.dataframe(
    stock_data,
    use_container_width=True
)
