import streamlit as st
from model import predict_va
from data_loader import load_data

st.title("DimABSA Sentiment Analyzer")

# Load dataset
data = load_data("dataset/eng_restaurant_trial_alltasks.jsonl")

st.subheader("Sample Dataset Example:")
st.write(data[0])

# Input
text = st.text_input("Enter sentence:")
aspect_input = st.text_input("Enter aspects (comma separated):")

if st.button("Analyze"):
    if text and aspect_input:
        aspects = aspect_input.split(",")

        st.subheader("Results:")

        for asp in aspects:
            asp = asp.strip()
            v, a = predict_va(text, asp)
            st.write(f"{asp} → {v}#{a}")