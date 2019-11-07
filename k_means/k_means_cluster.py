""" 
    skeleton code for k-means clustering mini-project

"""

import pickle
import numpy
import matplotlib.pyplot as plt
import sys
import pandas as pd
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than 4 clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
total_payments = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, total_payments]
data = featureFormat(data_dict, features_list )


# Alternative #1 to get min and max from github evykassirer (DOES NOT WORK WELL)
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(data)

print(min_max_scaler.data_min_)
print(min_max_scaler.data_max_)

poi, finance_features = targetFeatureSplit( data )

# Alternative #2 to get min and max from github jeremy-shannon (WORKS WELL)
salMin = 10000000
salMax = 0
for k in data_dict:
    sal = data_dict[k]["salary"]
    if sal != 'NaN':
        if sal < salMin:
            salMin = sal
        if sal > salMax:
            salMax = sal

print("min:", salMin)
print("max:", salMax)



df = pd.DataFrame(data_dict)
df2 = pd.DataFrame(df.transpose())
df2['exercised_stock_options'] = pd.to_numeric(df2['exercised_stock_options'], errors='coerce')
df2['salary'] = pd.to_numeric(df2['salary'], errors='coerce')

print(int(df2['exercised_stock_options'].max()))
print(int(df2['exercised_stock_options'].min()))

print(int(df2['salary'].max()))
print(int(df2['salary'].min()))


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, line below assumes 2 features)

################################################################
for f1, f2, _ in finance_features:
    plt.scatter( f1, f2 )
plt.show()
################################################################


# from sklearn.cluster import KMeans
# features_list = ["poi", feature_1, feature_2]
# data2 = featureFormat(data_dict, features_list )
# poi, finance_features = targetFeatureSplit( data2 )
# clf = KMeans(n_clusters=2)
# pred = clf.fit_predict( finance_features )
# Draw(pred, finance_features, poi, name="clusters_before_scaling.pdf", f1_name=feature_1, f2_name=feature_2)

#################################################################
from sklearn.cluster import KMeans
clf = KMeans(2)
clf.fit(finance_features)
pred = clf.predict(finance_features)
#################################################################

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

#################################################################
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters-x.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("no predictions object named pred found, no clusters to plot")
################################################################




