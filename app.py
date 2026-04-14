import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model
model, columns = pickle.load(open("model.pkl", "rb"))

# Page setup
st.set_page_config(page_title="Student AI Predictor", layout="wide")

# Sidebar Navigation
st.sidebar.title("📱 Navigation")
page = st.sidebar.radio("Go to", ["Login", "Dashboard", "Predict", "Results", "History"])

# ---------------- LOGIN PAGE ----------------
if page == "Login":
    st.markdown("<h1 style='text-align:center;'>🎓 Student Performance Predictor</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("LOGIN"):
            st.success("Login Successful!")

# ---------------- DASHBOARD ----------------
elif page == "Dashboard":
    st.title("👋 Welcome Student")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=200)

    st.markdown("### Choose an option:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("📊 Predict Performance")
    with col2:
        st.info("📈 View Results")
    with col3:
        st.warning("📜 History")

# ---------------- INPUT PAGE ----------------
elif page == "Predict":
    st.title("📥 Enter Student Details")

    col1, col2 = st.columns(2)

    with col1:
        attendance = st.slider("Attendance (%)", 0, 100)
        assignment = st.slider("Assignment Score", 0, 100)
        study_hours = st.slider("Study Hours", 0, 10)

    with col2:
        midterm = st.slider("Midterm Marks", 0, 100)
        final_exam = st.slider("Final Exam Marks", 0, 100)
        socialmedia_usage = st.slider("Social Media Usage", 0, 12)

    uploaded_file = st.file_uploader("📂 Upload CSV File (optional)")

    if st.button("🚀 Predict using AI"):
        input_df = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

        input_df["study_hours_per_day"] = study_hours
        input_df["attendance_percentage"] = attendance
        input_df["assignment_score"] = assignment
        input_df["midterm_score"] = midterm
        input_df["final_exam_score"] = final_exam
        input_df["socialmedia_usage"] = socialmedia_usage

        prediction = model.predict(input_df)[0]

        st.session_state["result"] = prediction
        st.success("Prediction Done! Go to Results Page")

# ---------------- RESULT PAGE ----------------
elif page == "Results":
    st.title("📊 Prediction Result")

    if "result" in st.session_state:
        score = st.session_state["result"]

        st.markdown(f"### 🎯 AI Confidence: {round(score,2)}%")

        # Circular progress (fake using progress bar)
        st.progress(int(score))

        if score < 50:
            st.error("⚠️ Status: AT RISK")
            st.write("Low performance detected. Improve study habits.")
        elif score < 75:
            st.warning("🙂 Status: AVERAGE")
        else:
            st.success("🏆 Status: EXCELLENT")

    else:
        st.info("No prediction yet")

# ---------------- HISTORY PAGE ----------------
elif page == "History":
    st.title("📜 Prediction History")

    history = [
        "20-Jan-2026 → Average",
        "18-Jan-2026 → At Risk",
        "15-Jan-2026 → Excellent",
        "12-Jan-2026 → Average"
    ]

    for h in history:
        st.write("➡️", h)

    if st.button("Clear History"):
        st.success("History Cleared!")