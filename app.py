import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Social Media Addiction Predictor",
    layout="centered"
)

st.title("AI-Based Early Social Media Addiction Risk Prediction")

st.write("Enter user details to predict addiction level")

age = st.slider("Age", 10, 40, 18)

daily_screen_time = st.slider(
    "Daily Screen Time (Hours)",
    0.0,
    15.0,
    5.0
)

social_media_hours = st.slider(
    "Social Media Usage Hours",
    0.0,
    15.0,
    4.0
)

study_hours = st.slider(
    "Study Hours",
    0.0,
    15.0,
    4.0
)

sleep_hours = st.slider(
    "Sleep Hours",
    0.0,
    12.0,
    7.0
)

notifications_per_day = st.slider(
    "Notifications Per Day",
    0,
    500,
    100
)

focus_score = st.slider(
    "Focus Score",
    0,
    100,
    50
)

productivity_score = st.slider(
    "Productivity Score",
    0,
    100,
    50
)

if st.button("Predict Addiction Level"):

    score = (
        social_media_hours +
        daily_screen_time +
        (notifications_per_day / 100)
        - sleep_hours
        - study_hours
        - (focus_score / 20)
        - (productivity_score / 20)
    )

    if score <= 3:
        result = "Low"

    elif score <= 8:
        result = "Medium"

    else:
        result = "High"

    st.success(f"Predicted Addiction Level: {result}")

    if result == "Low":

        st.info(
            "Healthy social media usage detected."
        )

    elif result == "Medium":

        st.warning(
            "Moderate addiction risk detected. "
            "Try reducing screen time and notifications."
        )

    else:

        st.error(
            "High addiction risk detected. "
            "Please maintain healthy digital habits."
        )

        st.subheader("Recommendations")

        st.write("• Reduce social media usage time")
        st.write("• Turn off unnecessary notifications")
        st.write("• Improve sleep schedule")
        st.write("• Increase study and focus time")
        st.write("• Take regular digital detox breaks")