### Description
This is a repo for the Natural Language Processing with Disaster Tweets (NLP with Disaster Tweets) Kaggle Competition. Due to the english language having certain words
be slang and not quite literal to the intended meaning of the actual word, some tweets may sound off. This project is an attempt to create a Natural Language Process code
that deciphers and identifies whether a tweets is announcing a literal disaster or if the tweet is being metaphorical. 

Kaggle Link: https://www.kaggle.com/competitions/nlp-getting-started/overview

## Project Website
https://jeampy.pythonanywhere.com

## Final Notebook


## Poster
https://drive.google.com/file/d/1lTDobSUjzXcmn8aI_4vq4aRdgQglRHlf/view?usp=sharing

## Final Report

# Kaggle-Spr2025 Team
Team - Alpharius

Client: Cengiz Gunay

Jonathan Tran - Project Manager and Data Analyst


Kazuki Susuki - Client Liaison and Data Visualizer


Jeampy Kalambayi - Data Modeler and Project Documentation

## Technologies
Google Colab - Used for data cleaning, analysis, visualization, and model training.

Jira - For task organization, project management, and scheduling.

Flask - For coding the website
## Project Usage
The usage of the NLP models is to classify the text in Twitter posts as disasters or not disasters. Each model uses a different set of algorithms to assign targets 1(Disaster) or 0(Not Disaster) to each tweet. Models are trained on a training dataset(train.csv) and then tested on a testing dataset(test.csv) for target assignment. The targets and the ID for each dataset are turned in to the Kaggle challenge to test the accuracy of our models.

# Project Status
Working Features:

1. Natural Language Processing: Each model can train on dataset and process text to assign a text as a disaster or not.

2. Demo: Using the BERT Model notebook, a user can input text and the model will assign that text as a disaster or not based on the training data.

# Project Datasets

https://www.kaggle.com/competitions/nlp-getting-started/data
Includes training dataset and testing dataset.

# ML/AI
Below are the listed models used for Natural Language Processing. Please see model's notebook for results.
### Support Vector Machine
Support Vector Machine (SVMs) is a supervised learning model that is used for classification, regression, and outliers detection. 
This type of algorithm allows data to be separated by margins and put into certain classifications. The results for SVMs are determined 
based on the data and parameters are used. In this case, kernel RBF is determined to be the best SVM result based on classification report. 
### BERT
BERT (Bidirectional Encoder Representations from Transformers) is a context-sensitive learning model used for classification tasks. It is an encoder-only
model that encodes input sequences into high dimensional embeddings.

## Main Results

## TODO:
Optimization: We want to focus on increasing the accuracy of the BERT model to get a higher place on the scoreboard for the Kaggle Competition.

Computer Vision: Some of the tweets include images of the disaster being described. We wanted to leverage computer vision to not only process text but also images for classification.

Improve ROC Curve: The ROC Curve is not correctly visualized with the true and false positives. 

Improve TSNE: The TSNE graph is not in 3D, we have only visualized it in 2D. 

