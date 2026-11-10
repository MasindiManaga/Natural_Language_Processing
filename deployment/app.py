# load libraries
from pathlib import Path

import joblib
import streamlit as st

# configure page
st.set_page_config(
    page_title="Researchly Abstract Classifier",
    page_icon="📄"
)

# load model
@st.cache_resource
def load_model():
    path = Path(__file__).parent / "research_classifier.joblib"

    if not path.exists():
        st.error("Model file not found. Please check the deployment folder.")
        st.stop()

    return joblib.load(path)


model = load_model()

# app interface
st.title("Researchly Research Abstract Classifier")

st.write(
    "This application classifies research abstracts "
    "as either AI-related or classical research."
)

abstract = st.text_area(
    "Enter research abstract:",
    height=200,
    placeholder="Paste a research abstract here..."
)

if st.button("Classify Abstract"):
    if not abstract.strip():
        st.warning("Please enter a research abstract.")
    else:
        prediction = model.predict([abstract])[0]

        st.markdown("### Prediction")
        st.success(f"The abstract is classified as: {prediction}")
