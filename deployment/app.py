# load libraries
import joblib
import streamlit as st

from pathlib import Path

# load model
path = Path(__file__).parent / "research_classifier.joblib"
model = joblib.load(path)

# app interface
st.title("Researchly Research Abstract Classifier")

st.write(
    "This app classifies reserch abstracts as either AI-related or classical research. "
)

abstract = st.text_area("Enter research abstract:", height=200)

if st.button("Classify Abstract"):
    st.markdown("### **Prediction**")
    if abstract.strip():
        prediction = model.predict([abstract])[0]
        st.success(f"The abstract is classified as: {prediction}")
    else:
        st.warning("Please enter a research abstract.")


