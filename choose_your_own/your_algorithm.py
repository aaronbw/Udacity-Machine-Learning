#!/usr/bin/python3

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


### *** import the classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier



### *** RandomForestClassifier
##~ 
##~ *** SKLEARN Examples
##~ clf = RandomForestClassifier(n_estimators=100, max_depth=2, 
##~                             random_state=0)
##~ clf.fit(X, y)
##~ 
##~ *** Predict
##~ print(clf.predict([[0, 0, 0, 0]]))
##~ 
##~ *** FROM GIT USER ***
##~ clf = RandomForestClassifier(n_estimators=100)
##~ clf = clf.fit(features_train, labels_train)
##~ 
##~ # print the accuracy and display the decision boundary
##~ print('Accuracy = {0}'.format(clf.score(features_test, labels_test)))
##~ 
##~ *** BEST (Accuracy = 0.924)
##~ clf = RandomForestClassifier(n_estimators=10)
##~ clf = clf.fit(features_train, labels_train)


### *** AdaBoostClassifier
##~ 
##~ *** SKLEARN Examples
##~ clf = AdaBoostClassifier(n_estimators=100, random_state=0)
##~ 
##~ clf.fit(X, y)
##~ 
##~ *** Predict
##~ clf.predict([[0, 0, 0, 0]])
##~ 
##~ *** FROM GIT USER ***
##~ clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=200)
##~ clf = clf.fit(features_train, labels_train)
##~ 
##~ # print the accuracy and display the decision boundary
##~ print 'Accuracy = {0}'.format(clf.score(features_test, labels_test))
##~ 
##~ *** BEST (Accuracy = 0.924)
##~ clf = AdaBoostClassifier(learning_rate=0.35)
##~ clf = clf.fit(features_train, labels_train)


### *** KNeighborsClassifier
##~ 
##~ *** SKLEARN Examples
##~ neigh = KNeighborsClassifier(n_neighbors=3)
##~ 
##~ neigh.fit(X, y)
##~ 
##~ *** FROM GIT USER ***
##~ 
##~ clf = KNeighborsClassifier(n_neighbors=1)
##~ clf.fit(features_train, labels_train)
##~ 
# print the accuracy and display the decision boundary
##~ print 'Accuracy = {0}'.format(clf.score(features_test, labels_test))
##~ 
##~ *** BEST (Accuracy = 0.)
clf = KNeighborsClassifier(n_neighbors=8)
clf = clf.fit(features_train, labels_train)



print('Accuracy = {0}'.format(clf.score(features_test, labels_test)))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
