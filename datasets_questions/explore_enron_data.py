#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))


### Lesson 13 - How many data points (people) are in the Enron dataset?
print('Number of people in the Enron dataset: {0}'.format(len(enron_data)))

### Lesson 14 - For each person in the Enron dataset, how many features are available?
values = list(enron_data.values())
print('Number of features for each person in the Enron dataset: {0}'.format(len(values[0])))

### Lesson 15 - How many POIs are there in the Enron dataset?
pois = [x for x, y in enron_data.items() if y['poi']]
print('Number of POI\'s: {0}'.format(len(pois)))

### Quiz 18-20
### 18 - What is the total value of the stock belonging to James Prentice?
### 19 - How many email messages do we have from Wesley Colwell to persons of interest?
### 20 - What’s the value of stock options exercised by Jeffrey K Skilling?
print('James Prentice\'s total stock value:', enron_data['PRENTICE JAMES']['total_stock_value'])

print('Number of emails from Wesley Colwell to persons of interest:', enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print('Value of stock options exercised by Jeffrey K Skilling', enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

### Quiz 25 - Of these three individuals (Lay, Skilling and Fastow), who took home the most money?
### How much money did that person get?
names = ['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']
names_payments = {name:enron_data[name]['total_payments'] for name in names}
print('Who took home the most money?', sorted(names_payments.items(), key=lambda x: x[1], reverse=True))

### Quiz 27
### How many folks in this dataset have a quantified salary?
import pandas as pd
df = pd.DataFrame(enron_data)
print('Number of people with a quantified salary: {0}' .format(sum(df.loc['salary',:] != 'NaN')))
### What about a known email address?
print('Number of people with a known email address: {0}' .format(sum(df.loc['email_address',:] != 'NaN')))

### Quiz 29
### How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? 
### What percentage of people in the dataset as a whole is this?
isnan = sum(df.loc['total_payments',:]=='NaN')
_,cols = df.shape
print('Number of people with Total Payments of "NaN": {0} people = {1:.2f}%' .format(isnan, 100.*isnan/cols))

### Quiz 30
### How many POIs in the E+F dataset have “NaN” for their total payments?
### What percentage of POI’s as a whole is this?
isnan = sum(df.loc['total_payments',pois]=='NaN')
print('Number of POIs with Total Payments of "NaN": {0} people = {1:.2f}%' .format(isnan, 100.*isnan/cols))


### Quiz 26 - How is it denoted when a feature doesn’t have a well-defined value?
### NaN returned for values that are not numbers (Not a Number)
### print(enron_data['PRENTICE JAMES'])

### *** Quiz 16 NOT NECCESSARY ***
### f = open("../final_project/poi_names.txt", "r")
### lines = f.readlines()
### f.close()
### user_search_value = "("
### count = 0
### for line in lines:
###     line = line.strip().lower().split()
###     for words in line:
###         if words.find(user_search_value.lower()) != -1:
###             count += 1
### print("\nYour search value of '%s' appears %s times in this file" % (user_search_value, count))

### *** Quiz 14 P2 to P3 ***
### print('Number of features for each person in the Enron dataset: {0}'.format(len(enron_data.values()[0])))
### {names[i]:d.values()[i] for i in range(len(names))}
### 
### dict(zip(names, d.values()))
### 
### values = list(d.values())
### {name:values[i] for i,name in enumerate(names)}
