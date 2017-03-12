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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.naive_bayes import GaussianNB

clf_gnb = GaussianNB()

## fit
clf_gnb_fit_time = time()

clf_gnb.fit(features_train, labels_train)

print "training time:", round(time()-clf_gnb_fit_time, 3), "s"

## fit
clf_gnb_predict_time = time()

prediction = clf_gnb.predict(features_test)

print "prediction time:", round(time()-clf_gnb_predict_time, 3), "s"

## fit
clf_gnb_score_time = time()

accuracy = clf_gnb.score(features_test, labels_test)

print "score time:", round(time()-clf_gnb_score_time, 3), "s"

## accuracy
print "accuracy:", accuracy
#########################################################


