#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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


from sklearn.svm import SVC

clf_svc = SVC(kernel='rbf', C=10000)

clf_svc_fit_time = time()

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
clf_svc.fit(features_train, labels_train)

print "training time:", round(time()-clf_svc_fit_time, 3), "s"


pred = clf_svc_predict_time = time()

predictions = clf_svc.predict(features_test)

print "predict time:", round(time()-clf_svc_predict_time, 3), "s"


clf_svc_score_time = time()

accuracy = clf_svc.score(features_test, labels_test)

print "score time:", round(time()-clf_svc_score_time, 3), "s"


print "accuracy:", accuracy

i = 0

for j in range(len(predictions)):
    if predictions[j] == 1:
        i = i + 1

print "Chris:", i

#########################################################
### your code goes here ###

#########################################################


