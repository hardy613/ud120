#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


clf = DecisionTreeClassifier()

features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.3, random_state=42)

clf = clf.fit(features_train, labels_train)

print "F1 score:", clf.score(features_test, labels_test)
# test
print "test data poi:", labels_test.count(1.0)
print "test total people:", len(labels_test)
# train
print "train data poi:", labels_train.count(1.0)
print "train total people:", len(labels_train)
# predict
pred = clf.predict(features_test)

cm = metrics.confusion_matrix(labels_test, pred)

print "confusion matrix\n", cm
print "precision", metrics.precision_score(labels_test, pred)
print "recall", metrics.recall_score(labels_test, pred)

## example data from prof
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print metrics.confusion_matrix(true_labels, predictions)

print "precision", metrics.precision_score(true_labels, predictions)
print "recall", metrics.recall_score(true_labels, predictions)
