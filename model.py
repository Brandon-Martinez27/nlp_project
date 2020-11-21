from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction import text 

import pandas as pd
import numpy as np


stop_words_eng = text.ENGLISH_STOP_WORDS
add_stopwords = ['file', 'import', 'use', 
        'return', 'also', 'code', 'using', 'see', 
        'install', 'default', '10', '100', '1000', 
        '11', '12', '15', '20', '27', '30', '35', 
        '36', '40', 'able', 'access', 'account', 
        'action', 'active', 'actually', 'add', 
        'avoid', 'awesome']
my_stop_words = text.ENGLISH_STOP_WORDS.union(add_stopwords)

def bow_fe(train, validate, test):
    vectorizer = CountVectorizer(stop_words=my_stop_words, 
                             min_df=10, 
                             ngram_range=(1,2), 
                             binary=True)
    # Learn vocabulary in sentences. 
    vectorizer.fit(train.clean)

    # Get dictionary. 
    vectorizer.get_feature_names()

    # Transform each sentences in vector space
    X_train = vectorizer.transform(train.clean)
    X_validate = vectorizer.transform(validate.clean)
    X_test = vectorizer.transform(test.clean)
    return X_train, X_validate, X_test

def tfidf_fe(train, validate, test):
    # Transform the clean text into sparse matrix
    tfidf = TfidfVectorizer(stop_words= my_stop_words, 
                            min_df=8, 
                            ngram_range=(1,2), 
                            binary=True)
    # Fit on cleaned text in train
    tfidf = tfidf.fit(train.clean)

    # Get vocabularies.
    tfidf.vocabulary_

    # Transform the train and validate
    X_train = tfidf.transform(train.clean)
    X_validate = tfidf.transform(validate.clean)
    X_test = tfidf.transform(test.clean)
    return X_train, X_validate, X_test

def tfidf_fe_test(train, test):
    # Transform the clean text into sparse matrix
    tfidf = TfidfVectorizer(stop_words= my_stop_words, 
                            min_df=8, 
                            ngram_range=(1,2), 
                            binary=True)
    # Fit on cleaned text in train
    tfidf = tfidf.fit(train.clean)

    # Get vocabularies.
    tfidf.vocabulary_

    # Transform the New test data
    X_test = tfidf.transform(test.clean)
    return X_test