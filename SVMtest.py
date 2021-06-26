#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:01:48 2019

@author: jyothyrajs
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix

#%matplotlib inline

bankdata=pd.read_csv("IA.csv");
bankdata.shape
bankdata.head()
#dividing data into attributes and labels
X=bankdata.drop('USN',axis=1)
y=bankdata['USN']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.20)
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train,y_train)
y_pred=svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))