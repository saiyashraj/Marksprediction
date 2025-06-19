import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("exam_score.pkl")

# Page setup
st.set_page_config(page_title="Exam Score Predictor", page_icon="📘", layout="centered")

# Title
st.title("📘 Student Exam Score Predictor")
st.markdown("Enter the student's details below to predict their exam score:")

# Inputs
study_hours = st.slider("📚 Study Hours per Day", 0.0, 12.0, 2.0)
attendance = st.slider("🏫 Attendance Percentage", 0.0, 100.0, 80.0)
mental_health = st.slider("🧠 Mental Health Rating (1–10)", 1, 10, 5)
sleep_hours = st.slider("😴 Sleep Hours per Night", 0.0, 12.0, 7.0)
part_time_job = st.selectbox("💼 Do you have a Part-Time Job?", ["No", "Yes"])
ptj_encoded = 1 if part_time_job == "Yes" else 0

# Predict button
if st.button("🔍 Predict Exam Score"):
    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]])

    try:
        prediction = model.predict(input_data)[0]
        prediction = max(0, min(100, prediction))

        # Display prediction
        st.markdown("### 🎯 Predicted Exam Score:")
        st.success(f"{prediction:.2f} out of 100")

        # Add snow effect 🎉
        st.snow()

    except Exception as e:
        st.error(f"❌ Error in prediction: {e}")


