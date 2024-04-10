import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('../model/model.pkl')

st.title("AI Predictive Maintenance System")

st.write("Enter machine sensor values to predict failure.")

# Inputs
temp = st.slider("Temperature", 30, 100, 50)
vib = st.slider("Vibration", 0.0, 0.1, 0.03)
press = st.slider("Pressure", 20, 50, 30)

# Prediction
if st.button("Predict"):
    data = np.array([[temp, vib, press]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Machine Failure Likely")
    else:
        st.success("Machine Operating Normally")