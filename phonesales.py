import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model = pickle.load(open("smartphone_sales_model.pkl", "rb"))

# Streamlit UI
st.title("📱 Smartphone Sales Prediction")

# User Inputs
brand = st.selectbox("Select Brand", ["Apple", "Samsung", "OnePlus", "Xiaomi", "Other"])
price = st.number_input("Enter Price ($)", min_value=100, max_value=2000, value=500)
marketing_spend = st.number_input("Marketing Spend ($)", min_value=1000, max_value=500000, value=10000)
season = st.selectbox("Select Season", ["Winter", "Spring", "Summer", "Autumn"])
stock_availability = st.slider("Stock Availability (Units)", 100, 100000, 10000)

# Convert Categorical Data
brand_dict = {"Apple": 1, "Samsung": 2, "OnePlus": 3, "Xiaomi": 4, "Other": 5}
season_dict = {"Winter": 1, "Spring": 2, "Summer": 3, "Autumn": 4}

brand_num = brand_dict[brand]
season_num = season_dict[season]

# Make Prediction
if st.button("Predict Sales"):
    input_features = np.array([[brand_num, price, marketing_spend, season_num, stock_availability]])
    predicted_sales = model.predict(input_features)[0]
    st.success(f"📈 Estimated Sales: {int(predicted_sales)} units")
