#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess




features_train, features_test, labels_train, labels_test = preprocess()




from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


##count = len(["ok" for idx, label in enumerate(labels_test) if label == pred[idx]])
##accuracy = (float(count) / len(labels_test))
count =0;
name_pred = "No"
name_label = "No"
for idx, label in enumerate(labels_test):
    if pred[idx] == 1:
        name_pred = "UnaBomber"
    else:
        name_pred = "No"
    if label == 1:
        name_label = "UnaBomber"
    else:
        name_label = "No"
    print "prediccion", pred[idx], "=",name_pred,  " valor real", label, "=",name_label

    print
    count+=1
    if count == 50:
        break
   
    
accuracy = accuracy_score(labels_test, pred)

print accuracy

