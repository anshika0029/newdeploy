import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('home_price_model.pkl')

# Streamlit UI
st.title("🏠 Home Price Prediction App")

# Input fields
area = st.number_input("Enter the area in square feet:", min_value=100, max_value=10000, value=1500)

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[area]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Price: ₹{prediction[0]:,.2f}")
