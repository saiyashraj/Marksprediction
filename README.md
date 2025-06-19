# Marksprediction
ML Model which Predicts Student Marks Based on Input
# 📘 Student Exam Score Predictor

This Streamlit web app predicts a student's exam score based on their study habits, attendance, sleep, mental health, and whether they have a part-time job.

## 🔍 Features

- 📚 Input daily study hours using a slider
- 🏫 Set attendance percentage
- 🧠 Rate mental health on a scale of 1 to 10
- 😴 Choose average sleep hours per night
- 💼 Select whether the student has a part-time job
- 🎯 Predicts exam score out of 100 using a trained machine learning model
- ❄️ Fun snowflake animation on prediction

## 🛠 Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- Scikit-learn (for the trained ML model)
- NumPy
- Joblib (for loading the saved model)

## 🧠 Model Info

The app uses a pre-trained Linear Regression model (`exam_score.pkl`) built with 5 features:
1. Study hours per day
2. Attendance percentage
3. Mental health rating
4. Sleep hours per night
5. Part-time job (encoded as 0 or 1)

## 🚀 How to Run the App Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/exam-score-predictor.git
    cd exam-score-predictor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure the file `exam_score.pkl` (trained model) is in the same directory.

4. Run the app:
    ```bash
    streamlit run exam_score.py
    ```

## 📦 Requirements

Create a `requirements.txt` with:
```txt
streamlit
numpy
scikit-learn
joblib
