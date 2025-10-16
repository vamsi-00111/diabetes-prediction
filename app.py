import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and preprocessor
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("artifacts/preprocessed.pkl", "rb") as f:
    preprocessor = pickle.load(f)

# App title
st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient details below to estimate the likelihood of diabetes:")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
bloodpressure = st.number_input("Blood Pressure", min_value=0, max_value=122, value=70)
skinthickness = st.number_input("Skin Thickness", min_value=0, max_value=99, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=846, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=67.1, value=25.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=21, max_value=81, value=33)

if st.button("Predict"):
    # Arrange input in the exact order your model expects
    input_data = pd.DataFrame([[
        glucose, bloodpressure, skinthickness, insulin, bmi, age, pregnancies, diabetes_pedigree
    ]], columns=[
        'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age', 'Pregnancies', 'DiabetesPedigreeFunction'
    ])

    # Apply preprocessing
    input_scaled = preprocessor.transform(input_data)

    # Predict probability
    prob = model.predict_proba(input_scaled)[0][1]
    percent = round(prob * 100, 2)

    # Display result
    st.subheader(f"🧮 The person has a **{percent}%** chance of having diabetes.")
    if percent >= 50:
        st.error(f"🚨 High risk of diabetes ({percent}%)")
    else:
        st.success(f"✅ Low risk of diabetes ({percent}%)")
