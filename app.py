import streamlit as st
import numpy as np
from stable_baselines3 import PPO

# Load model
model = PPO.load("models/hospital_model")

st.set_page_config(page_title="Hospital AI", layout="centered")

st.title("🏥 AI Hospital Resource Optimizer")

st.write("Provide hospital conditions and get AI decision")

beds = st.slider("Available Beds", 0, 100, 50)
icu = st.slider("Available ICU Units", 0, 20, 10)
patients = st.slider("Incoming Patients", 1, 20, 5)

severity = st.selectbox("Patient Severity", ["Low", "Medium", "Critical"])

severity_map = {"Low": 0, "Medium": 1, "Critical": 2}

state = np.array([beds, icu, patients, severity_map[severity]])

if st.button("Get AI Decision"):
    action, _ = model.predict(state)

    if action == 0:
        st.success("🛏️ Assign to Bed")
    elif action == 1:
        st.success("🚑 Assign to ICU")
    else:
        st.warning("⏳ Put in Waiting")

    st.info(f"Input State: {state}")