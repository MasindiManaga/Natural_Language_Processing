# Expert System

1. Overview

This section covers data loading, data exploration, preprocessing and text denoising, feature engineering, baseline modelling, and baseline model evaluation for the Research Papers – Expert System.

The objective is to prepare the research abstract dataset for the development of a machine learning approach that classifies research documents based on their text.

2. Dataset

2.1 Dataset Structure

The research_abstracts.json dataset was loaded and converted into a Pandas
DataFrame for exploration and preprocessing.

Initial observations: 1,138

Original columns:

• DOI

• Abstract

• Label


Input:

• Abstract


Target:

• Label


Target classes:

• ai

• classical


2.2 Target Distribution

The original dataset contains two target classes:

• classical: 900

• ai: 238

The target distribution shows that the dataset contains more classical
observations than ai observations.

3. Data Preprocessing

3.1 Missing Values

The dataset was inspected for missing values before text preprocessing.

Missing DOI values identified: 4

The records containing missing DOI values were removed from the dataset.

Observations after missing-value removal: 1,134

3.2 Duplicate Records

The dataset was also inspected for duplicate abstracts.

Duplicate abstracts identified during initial exploration: 13

After records containing missing DOI values were removed, duplicate records
were removed based on the Abstract column.

Observations after preprocessing: 1,123

3.3 Text Denoising

A cleaned version of the Abstract column was created and stored in the
Clean_Abstract column.

The text denoising process included:

• Converting text to lowercase.
• Removing URLs.
• Removing email addresses.
• Removing DOI-style URLs.
• Removing unwanted special characters and punctuation while retaining
letters, numbers, whitespace, and hyphens.
• Removing unnecessary whitespace.

The purpose of the denoising stage was to reduce irrelevant textual elements
before feature representation.

3.4 Preprocessing Validation

The cleaned dataset was validated after preprocessing to check for missing
and empty values.

Validation results:

• Missing Clean_Abstract: 0
• Missing Label: 0
• Empty Clean_Abstract: 0
• Final observations: 1,123

The cleaned abstracts and their corresponding labels were retained for the
feature engineering stage.

4. Feature Engineering

4.1 Input and Target Features

The cleaned research abstracts were selected as the model input, while the
document category was selected as the target variable.

Input (X):

• Clean_Abstract

Target (y):

• Label

Therefore, each observation consists of a cleaned research abstract and its
corresponding classification label.

4.2 Feature Representation

Term Frequency–Inverse Document Frequency (TF-IDF) was used to convert the cleaned research abstracts into numerical feature representations suitable for machine learning.

TF-IDF represents documents based on the importance of terms within each document relative to their occurrence across the dataset.

The vectoriser was fitted using the training data only to prevent information from the test dataset influencing the feature representation.

4.3 BERT Embeddings

BERT embeddings were explored as an alternative approach to representing research abstracts.

Unlike TF-IDF, BERT uses contextual representations that can capture relationships between words based on their surrounding text.

The final baseline and classification experiments used TF-IDF. BERT was not included in the final model comparison.

5. Baseline Model

A baseline classification model was developed to establish an initial performance benchmark for the research abstract classification task.

The dataset was divided into training and testing subsets using a stratified 80/20 split to preserve the distribution of the two target classes.

6. Baseline Model Evaluation

The baseline classifier was evaluated using the held-out test dataset.

The evaluation considered accuracy and macro-averaged F1-score.

Baseline results:

- Accuracy: 79.1%

- Macro F1-score: 0.442

The baseline accuracy reflects the imbalance between the two target classes, with classical abstracts representing the majority of observations.

The macro F1-score provides a more balanced assessment by giving equal weight to both classes.
