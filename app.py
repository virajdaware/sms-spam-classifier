import streamlit as st

st.title("📩 SMS Spam Classifier")

msg = st.text_area("Enter your message")

if st.button("Predict"):
    if msg.strip() == "":
        st.warning("Please enter a message")
    else:
        st.success("App is working! Model will be connected next.")
