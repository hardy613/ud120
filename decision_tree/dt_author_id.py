#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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


from sklearn.tree import DecisionTreeClassifier

clf_dt = DecisionTreeClassifier(min_samples_split=40)

## fit
clf_dt_fit_time = time()

clf_dt.fit(features_train, labels_train)

print "training time:", round(time()-clf_dt_fit_time, 3), "s"

## fit
clf_dt_predict_time = time()

prediction = clf_dt.predict(features_test)

print "prediction time:", round(time()-clf_dt_predict_time, 3), "s"

## fit
clf_dt_score_time = time()

accuracy = clf_dt.score(features_test, labels_test)

print "score time:", round(time()-clf_dt_score_time, 3), "s"

## accuracy
print "accuracy:", accuracy

print "length:", len(features_train[0])

#########################################################


