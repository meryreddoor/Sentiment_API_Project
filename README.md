# ‘Sentiment API’ Project

The purpose of this project is to build an API from the scratch.
The API analyzes texts and determines its polarity and its subjectivity(sentiment). 
Also, it establishes the affinity between people. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
from mongoConnection import user_mydb,user_mycol
from mongoConnection import group_mydb,group_mycol
from bson.json_util import dumps
from pymongo import MongoClient
from flask import Flask, request
import pandas as pd
import numpy as np
import nltk
import json
```

### Installing

A step by step series of links that tell you how to run the project:

* [Count Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) - This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix

* [NLTK](https://www.nltk.org/api/nltk.sentiment.html) - This a tool to implement and facilitate Sentiment Analysis tasks using NLTK features and classifiers, especially for teaching and demonstrative purposes


## Main points covered

1. Write an API in MongoDB just to store chat messages in a database like mongodb or MySQL.

2. Extract sentiment from chat messages and perform a report over a whole conversation

3. Recommend friends to a user based on the contents from chat `documents` using a recommender system with `NLP` analysis.

## Demo

You can find a `demo` in `output` folder in order to understand how the API works.

* [Demo API Link](https://github.com/meryreddoor/Chat_Project/blob/ramaChat/output/demo_api.ipynb)

## Built With

* [Kaggle](https://www.kaggle.com/pierremegret/dialogue-lines-of-the-simpsons) - The dataset used

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - It provides tools, libraries and technologies that allows you to build a web application.