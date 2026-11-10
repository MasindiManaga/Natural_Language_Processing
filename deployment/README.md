# Researchly Research Abstract Classifier: Deployment Guide

## Overview

This folder contains the Streamlit web interface developed for ITNPA4-34: Natural Language Processing with Python, Project 1, Questions 1 and 2. The application accepts a research abstract and predicts one of two labels: ai or classical.

The exported model is a fitted scikit-learn pipeline combining TF-IDF text vectorisation and Linear Support Vector Classification (LinearSVC). The app loads the pipeline with Joblib, so it does not need the training dataset or notebooks to make predictions.

## Files

Natural_Language_Processing/
├── deployment/
│   ├── app.py
│   ├── research_classifier.joblib
│   └── README.md
├── requirements.txt
├── data/
├── docs/
└── notebooks/

`app.py` and `research_classifier.joblib` are put inside deployment/ together, because the application looks for the model beside the Python script.

## Requirements

- Python 3.11 or 3.12 is recommended for deployment.
- Python packages: streamlit, joblib, and scikit-learn.
- The model was saved with scikit-learn 1.7.2. Use this version when loading the model to avoid version-mismatch warnings.

## Run locally

From the repository root, open a terminal and run:

1. Create a virtual environment:

```bash
    python -m venv .venv
```

2. Activate it:
**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

3. Install the deployment dependencies:

```bash
python -m pip install streamlit joblib scikit-learn==1.7.2
```

4. Start the app:

```bash
python -m streamlit run deployment/app.py
```

5. Open the local address displayed in the terminal

## Use the classifier

1. Paste a research abstract into the text area.
2. Select Classify Abstract.
3. Read the predicted label (ai or classical).

If the text area is empty, the application displays a warning instead of making a prediction.

## Deploy with Streamlit Community Cloud

1. Push the repository to GitHub. Ensure that deployment/app.py, deployment/research_classifier.joblib, and the required dependency file are committed. Do not commit .venv/.
2. Open Streamlit Community Cloud and sign in with GitHub.
3. Choose Create app and select the repository and branch.
4. Set the main file path to deployment/app.py.
5. Ensure the dependency file used by the deployment pins scikit-learn==1.7.2. The root requirements.txt is the simplest default location to configure for Streamlit Cloud.
6. Deploy the app then enter a non-empty sample abstract and confirm that a prediction appears.

A successful cloud deployment should display the Researchly Research Abstract Classifier title, a text entry area, and a Classify Abstract button.

## Troubleshooting

| Problem | Check |
| --- | --- |
| `Model file not found` | Keep `research_classifier.joblib` in the same folder as `app.py` and commit it to GitHub. |
| `ModuleNotFoundError` | Install the missing package in the active environment and include it in deployment dependencies. |
| scikit-learn version warning | Use `scikit-learn==1.7.2`, the version used to save this model. |
| App does not launch | Run `python -m streamlit run deployment/app.py` from the repository root and inspect the terminal error. |
| Empty input | Enter an abstract before selecting **Classify Abstract**. |

## Assessment context

This deployment supports Question 2.3; web interface for the selected classification configuration and the deployment documentation required by Question 4.3. The modelling and evaluation steps are available in notebooks/01_expert_system.ipynb and notebooks/02_abstract_classifier.ipynb, with further explanation in docs/.
