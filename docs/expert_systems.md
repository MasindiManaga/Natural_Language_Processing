Expert System

1. Overview

This section covers data loading, data exploration, preprocessing and text
denoising, feature engineering, baseline modelling, and baseline model
evaluation for the Research Papers – Expert System.

The objective is to prepare the research abstract dataset for the development
of a machine learning approach that classifies research documents based on
their text.

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

To be documented after implementation.

4.3 BERT Embeddings

BERT embeddings have been identified for investigation as a feature
representation technique.

Implementation and results will be documented after completion.


5. Baseline Model

To be documented after implementation.


6. Baseline Model Evaluation

To be documented after implementation.
