#!/usr/bin/python

""" 
    Naive Bayes para predecir si las cartas son del UNABOMBER o No
    UNABOMBER  1
    NO UNABOMBER  1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess



## DATA
## EXTRAEMOS LA DATA DE ENTRENAMIENTO Y PRUEBA
features_train, features_test, labels_train, labels_test = preprocess()

## IMPORTAMOS LAS LIBRERIAS
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

## CREAMOS EL MODELO NAIVE BAYES
clf = GaussianNB()

## ENTRENAMOS
clf.fit(features_train, labels_train)

## PREDECIMOS
pred = clf.predict(features_test)


count =0;
name_pred = "No"
name_label = "No"

## IMPRIMIMOS RESULTADOS
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
    count+=1
    if count == 10:
        break

## CALCULAMOS LA EXACTITUD      
accuracy = accuracy_score(labels_test, pred)

## IMPRIMIMOS LA EXACTITID
print accuracy

