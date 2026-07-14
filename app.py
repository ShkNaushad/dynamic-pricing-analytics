import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("dynamic_pricing_model.pkl")

st.set_page_config(page_title="Dynamic Pricing Analytics", page_icon="💰")

st.title("💰 Dynamic Pricing Analytics")
st.write("Enter product details and click Predict Price.")

current_price = st.number_input("Current Price", min_value=0.0)
competitor_price = st.number_input("Competitor Price", min_value=0.0)
stock = st.number_input("Stock", min_value=0)
units_sold = st.number_input("Units Sold", min_value=0)
rating = st.number_input("Rating", min_value=0.0, max_value=5.0, step=0.1)
discount = st.number_input("Discount Percentage", min_value=0.0)
demand = st.number_input("Demand Index", min_value=0.0)

if st.button("Predict Price"):

    data = pd.DataFrame([[
        current_price,
        competitor_price,
        stock,
        units_sold,
        rating,
        discount,
        demand
    ]], columns=[
        "Current_Price",
        "Competitor_Price",
        "Stock",
        "Units_Sold",
        "Rating",
        "Discount_Percentage",
        "Demand_Index"
    ])

    prediction = model.predict(data)[0]

    st.success(f"✅ Recommended Price: ₹ {prediction:,.2f}")