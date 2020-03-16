# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:26:34 2020

@author: Harish
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("leaf.csv").as_matrix()

clf=DecisionTreeClassifier()



xtest=data[0:43:,2:]
leaf_label=data[0:43:,0]
clf.fit(xtest,leaf_label)

xtest=data[0:43:,2:]
actual_label=data[0:43:,0]
d=xtest[33]



print(clf.predict([xtest[33]]))



xtest=data[0:43:,2:]
leaf_label=data[0:43,1]
clf.fit(xtest,leaf_label)
clf.fit(xtest,leaf_label)

xtest=data[0:43:,2:]
actual_label=data[0:43:,0]
d=xtest[33]



print(clf.predict([xtest[33]]))