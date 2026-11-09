# Document Mining

## 1. Overview

This section covers research document loading, data exploration, text preprocessing and denoising, individual document summarisation, and aggregate document summarisation.

The objective is to process the supplied research articles and generate summaries that identify important information from the documents.

The cleaned research corpus is also prepared for the topic modelling stage.

## 2. Dataset

### 2.1 Dataset Structure

Five research articles were loaded from individual text files located in the `data` directory.

Source files:

- research_1.txt
- research_2.txt
- research_3.txt
- research_4.txt
- research_5.txt

The articles were loaded using Python and converted into a Pandas DataFrame.

Initial observations: 5

Columns created:

- article_id
- content
- word_count
- character_count

The `article_id` column identifies each research article.

The `content` column stores the original article text.

The `word_count` and `character_count` columns provide descriptive information about document length.

### 2.2 Dataset Exploration

The research corpus was inspected to confirm that all five documents had been loaded.

Document lengths were examined using word and character counts.

These measurements were used to understand differences in document size before preprocessing and summarisation.

## 3. Data Preprocessing

### 3.1 Missing Values

The research corpus was inspected for missing document content.

The purpose of this inspection was to identify documents that could not be processed due to missing text.

### 3.2 Duplicate Records

The corpus was inspected for duplicate records.

Duplicate checking was included to identify repeated documents that could influence subsequent text analysis.

### 3.3 Text Denoising

A cleaned version of the article content was prepared for text analysis.

The preprocessing stage aimed to reduce unnecessary textual elements while retaining the information required for summarisation and topic modelling.

The cleaned document content was stored separately from the original article text.

### 3.4 Preprocessing Validation

The cleaned corpus was inspected after preprocessing.

The purpose of validation was to ensure that the research documents remained available for summarisation and topic modelling.

The processed dataset was saved as:

`data/processed/cleaned_research_corpus.csv`

This dataset is reused during the topic modelling stage.

## 4. Individual Document Summarisation

### 4.1 Document Selection

The first research article, `research_1.txt`, was selected for individual summarisation.

The objective was to identify important sentences and produce a shorter representation of the original article.

### 4.2 Summarisation Approach

An extractive summarisation approach was used.

Extractive summarisation identifies and selects important sentences from the original document rather than generating entirely new sentences.

The approach uses the textual content of the document to determine which sentences should be included in the summary.

### 4.3 Summary Generation

The first research article was processed and summarised.

The selected sentences were combined to produce a shorter summary of the document.

The original article remained unchanged.

### 4.4 Summary Visualisation

A visualisation was produced to illustrate the sentence importance scores used during summarisation.

The visualisation supported the interpretation of which sentences contributed most strongly to the generated summary.

## 5. Aggregate Document Summarisation

### 5.1 Document Selection

The remaining four research articles were selected for aggregate summarisation.

Selected documents:
- research_2.txt
- research_3.txt
- research_4.txt
- research_5.txt

The objective was to identify important information across multiple research articles.

### 5.2 Aggregate Summarisation Approach

The remaining documents were combined for text analysis.

An extractive summarisation approach was applied to identify important sentences across the combined document collection.

The approach aimed to produce a summary representing information from the selected articles.

### 5.3 Aggregate Summary Generation

Important sentences were selected from the combined research corpus.

The selected sentences were used to construct an aggregate summary.

This provided a condensed representation of the information contained in the four documents.

### 5.4 Aggregate Summary Visualisation

A visualisation was produced to show the sentence importance scores used during aggregate summarisation.

The visualisation supported the interpretation of the selected summary content.

## 6. Topic Modelling Preparation

### 6.1 Cleaned Corpus

The cleaned research corpus was retained for subsequent topic modelling.

The processed dataset contains the document information required for further text analysis.

### 6.2 Dataset Reuse

The topic modelling notebook loads the cleaned research corpus directly from the `data/processed` directory.

This avoids repeating the document loading and preprocessing stages.

## 7. Conclusion

The Document Mining stage demonstrated the preparation and analysis of research documents using Python.

Five research articles were loaded into a structured DataFrame and prepared for text analysis.

Individual summarisation was performed on the first research article, while aggregate summarisation was applied to the remaining four articles.

The cleaned corpus was retained for subsequent topic modelling.
