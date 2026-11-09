# Abstract Classifier

## 1. Overview

This section covers machine learning model development, model comparison, performance improvement, model evaluation, and deployment for the Research Papers – Expert System.

The objective is to develop and evaluate machine learning models capable of classifying research abstracts into their corresponding categories using the cleaned dataset prepared during the Expert System stage.

## 2. Dataset

### 2.1 Dataset Structure

The `cleaned_research_abstracts.csv` dataset was loaded from the `data/processed` directory and converted into a Pandas DataFrame.

The dataset was prepared during the preprocessing stage documented in the Expert System.

Observations after preprocessing: 1,125

Input:

- Clean_Abstract

Target:

- Label

Target classes:

- ai
- classical

### 2.2 Data Preparation

The cleaned abstracts were selected as the model input, while the corresponding classification labels were selected as the target variable.

Input (X):

- Clean_Abstract

Target (y):

- Label

The dataset was divided into training and testing subsets using a stratified 80/20 split.

Stratification was applied to preserve the relative distribution of the target classes.

The same data split was used for model comparison to ensure consistent evaluation.

## 3. Feature Engineering

### 3.1 TF-IDF Vectorisation

Term Frequency–Inverse Document Frequency (TF-IDF) was used to convert the cleaned research abstracts into numerical features.

TF-IDF assigns weights to terms based on their frequency within individual documents and their frequency across the document collection.

The vectoriser was fitted using training data only to prevent data leakage.

### 3.2 Classification Pipeline

Machine learning pipelines were used to combine TF-IDF vectorisation with classification algorithms.

The pipelines ensured that the same feature extraction approach was applied during model training and prediction.

## 4. Machine Learning Models

### 4.1 Model Selection

Four classification algorithms were implemented for comparison:

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Classification (LinearSVC)
- Random Forest

These models were selected to compare different approaches to text classification.

### 4.2 Model Training

Each model was trained using the training subset of the cleaned research abstracts.

The same training and testing subsets were maintained across the four models.

Model performance was evaluated using the held-out test dataset.

### 4.3 Model Comparison

The classification models were compared using accuracy and macro-averaged F1-score.

Previously recorded test results:

| Model | Accuracy |
|---|---:|
| Multinomial Naive Bayes | 80.4% |
| Logistic Regression | 90.7% |
| LinearSVC | 92.4% |
| Random Forest | 91.6% |

LinearSVC achieved the highest accuracy among the four models.

The macro F1-score was also considered because the dataset contains an unequal distribution of the two target classes.

## 5. Model Performance Improvement

### 5.1 Hyperparameter Optimisation

Hyperparameter optimisation was applied to LinearSVC to investigate whether its classification performance could be improved.

The optimisation process used cross-validation on the training dataset to compare parameter configurations.

The held-out test dataset was reserved for final evaluation.

### 5.2 Optimisation Results

The tuned LinearSVC achieved a previously recorded test accuracy of 92.4%.

The optimisation process did not produce an improvement in test accuracy over the original LinearSVC model.

The result indicates that the original configuration already provided strong performance on the available dataset.

## 6. Model Evaluation

### 6.1 Evaluation Metrics

The classification models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Accuracy measured the proportion of correctly classified abstracts.

Precision and recall assessed classification performance for each target class.

The F1-score provided a combined measure of precision and recall.

### 6.2 Final Model Performance

LinearSVC achieved the highest previously recorded classification accuracy.

Accuracy: 92.4%

Macro F1-score: 0.879

The confusion matrix was used to examine correct and incorrect predictions across the two target classes.

These results demonstrate that the trained classifier performed better than the majority-class baseline established during the Expert System stage.

## 7. Model Deployment

### 7.1 Model Export

The selected trained classification pipeline was saved using Joblib.

Saved model:

- `deployment/research_classifier.joblib`

The saved pipeline contains the components required to transform cleaned research text and generate predictions.

Run App:
`python -m streamlit run deployment/app.py`

### 7.2 Web Interface

A Streamlit web interface was prepared to allow users to submit research abstracts for classification.

The application is designed to load the saved model and predict whether the submitted abstract belongs to the ai or classical category.

### 7.3 Deployment Validation

The exported model and application code were prepared for deployment.

Interactive testing of the Streamlit interface remains to be completed.

## 8. Conclusion

The Abstract Classifier stage demonstrated the application of supervised machine learning to research abstract classification.

Four algorithms were trained and evaluated using the same cleaned dataset.

LinearSVC achieved the strongest recorded classification accuracy, while hyperparameter optimisation did not improve the held-out test accuracy.

The selected model was exported for integration into a web-based classification interface.
