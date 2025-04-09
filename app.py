import streamlit as st
import joblib
import pandas as pd

model = joblib.load('aqi_model.pkl')

st.title('Air Quality Category Prediction')

st.markdown("Enter the air pollutant levels to predict the AQI category:")

a1 = st.number_input("PM2.5 (µg/m³)", min_value=0.0)
a2 = st.number_input("PM10 (µg/m³)", min_value=0.0)
a3 = st.number_input("NO2 (ppb)", min_value=0.0)
a4 = st.number_input("CO (ppm)", min_value=0.0)
a5 = st.number_input("O3 (ppb)", min_value=0.0)
a6 = st.number_input("Temperature (°C)", min_value=-30.0, max_value=60.0)
a7 = st.number_input("NO (ppb)", min_value=0.0)

if st.button('Predict'):
    input_data = pd.DataFrame([[a1, a2, a3, a4, a5, a6, a7]], columns=[
        'PM2.5 (µg/m³)', 'PM10 (µg/m³)', 'NO2 (ppb)', 'CO (ppm)',
        'O3 (ppb)', 'Temperature (°C)', 'NO (ppb)'
    ])
    result = model.predict(input_data)[0]
    st.success(f"Predicted AQI Category: **{result}**")
