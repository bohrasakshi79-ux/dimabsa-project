import streamlit as st
from transformers import pipeline

st.title("Aspect-Based Sentiment Analyzer")

classifier = pipeline("sentiment-analysis")

sentence = st.text_area("Enter sentence:")
aspects = st.text_input("Enter aspects (comma separated):")

if st.button("Analyze"):
    if sentence and aspects:
        aspect_list = aspects.split(",")

        st.subheader("Overall Sentiment")
        overall = classifier(sentence)[0]
        st.write(overall["label"])

        st.subheader("Aspect-wise Sentiment")
        for aspect in aspect_list:
            aspect = aspect.strip()
            result = classifier(f"{aspect} {sentence}")[0]
            st.write(f"{aspect} → {result['label']}")