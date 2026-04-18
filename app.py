import streamlit as st

st.title("Local Activity Connect")

activity = st.text_input("Enter an activity")
location = st.text_input("Enter location (optional)")

if st.button("Post Activity"):
    if activity:
        st.success(f"Activity posted: {activity} at {location}")
    else:
        st.warning("Please enter an activity")