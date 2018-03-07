#!/usr/bin/python

import pickle
import cPickle
import numpy


from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif



words_file = "../tools/word_data.pkl"
authors_file="../tools/email_authors.pkl"
""" 
        this function takes a pre-made list of email texts (by default word_data.pkl)
        and the corresponding authors (by default email_authors.pkl) and performs
        a number of preprocessing steps:
            -- splits into training/testing sets (10% testing)
            -- vectorizes into tfidf matrix
            -- selects/keeps most helpful features

        after this, the feaures and labels are put into numpy arrays, which play nice with sklearn functions

        4 objects are returned:
            -- training/testing features
            -- training/testing labels

    """
### the words (features) and authors (labels), already largely preprocessed
### this preprocessing will be repeated in the text learning mini-project
authors_file_handler = open(authors_file, "r")
authors = pickle.load(authors_file_handler)
authors_file_handler.close()

words_file_handler = open(words_file, "r")
word_data = cPickle.load(words_file_handler)
words_file_handler.close()

print word_data[0]
print '\n'
print word_data[1]
print '\n'
print word_data[10000]
print '\n'
print word_data[10003]
print authors[0]
print authors[1]
print authors[10000]
print authors [10003]
