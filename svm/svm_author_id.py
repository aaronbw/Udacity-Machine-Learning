#!/usr/bin/python3

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("C:\\Users\\Leone\\Desktop\\ud120-projects\\tools")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### make sure you use // when dividing for integer division

### *** Partial training set
### *** features_train = features_train[:len(features_train)//100] 
### *** labels_train = labels_train[:len(labels_train)//100]


from sklearn.svm import SVC
clf = SVC(C=10000, kernel="rbf")
t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")
t0 = time()
pred = clf.predict(features_test)
print ("predicting time:", round(time()-t0, 3), "s")


from sklearn.metrics import accuracy_score
print(accuracy_score(pred, labels_test))


### *** Element predictions
answer=predictions[10]
print(answer)
### *** print("Element 10 =", pred[10])
### *** print("Element 26 =", pred[26])
### *** print("Element 50 =", pred[50])

print(sum(pred))