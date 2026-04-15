import streamlit as st
from transformers import pipeline
import re

# Page settings
st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        color: #4CAF50;
        font-size: 40px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: gray;
        font-size: 18px;
    }
    .result-box {
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        background-color: #ffffff;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">💬 Aspect-Based Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze sentiment for specific aspects in a sentence</div>', unsafe_allow_html=True)

# Input
sentence = st.text_area("📝 Enter Sentence", placeholder="Example: The food is great but service is bad")
aspects = st.text_input("🔍 Enter Aspects (comma separated)", placeholder="food, service")

# Load model
classifier = pipeline("sentiment-analysis")

# Button
if st.button("Analyze Sentiment"):

    if sentence and aspects:

        aspect_list = aspects.split(",")

        # 🔹 Overall sentiment
        overall = classifier(sentence)[0]

        st.markdown("### 📊 Overall Sentiment")
        if overall["label"] == "POSITIVE":
            st.success(f" {overall['label']}")
        else:
            st.error(f" {overall['label']}")

        # 🔹 Improved aspect logic (handles "but")
        st.markdown("### 🔎 Aspect-wise Sentiment")

        parts = re.split(r'\bbut\b', sentence.lower())

        for aspect in aspect_list:
            aspect = aspect.strip()
            found = False

            for part in parts:
                if aspect in part:
                    result = classifier(part)[0]
                    found = True
                    break

            if not found:
                result = classifier(sentence)[0]

            if result["label"] == "POSITIVE":
                st.markdown(f'<div class="result-box">✅ <b>{aspect}</b> → Positive</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="result-box">❌ <b>{aspect}</b> → Negative</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter both sentence and aspects")