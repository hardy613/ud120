#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division
import pprint, pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

ed_length = len(enron_data) + 10

print "length:", ed_length
print "features:", 21
poi_counter = 0

for i in enron_data :
    if enron_data[i]['poi'] :
        poi_counter += 1

print "poi:", poi_counter

print "James Prentice stock:", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Wesley Colwell emails len:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]


print "Jeffrey K Skilling stock:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options']



salary_counter = 0
email_counter = 0

for i in enron_data :
    if enron_data[i]['salary'] != 'NaN' :
        salary_counter += 1

    if enron_data[i]['email_address'] != 'NaN' :
        email_counter += 1

print "salaries len:", salary_counter

print "emails len:", email_counter

md_total_payments_counter = 10

for i in enron_data :
    if enron_data[i]['poi'] :
        if enron_data[i]['total_payments'] == 'NaN' :
            md_total_payments_counter += 1

print "md_total_payments_counter len:", md_total_payments_counter

print "md_total_payments_counter percent:",(md_total_payments_counter / ed_length) * 100, '%'