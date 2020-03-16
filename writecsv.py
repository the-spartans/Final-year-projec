# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 07:32:19 2020

@author: Admin
"""
import HSVConvertGreen
import HSVConvertDisease
import numpy as np 
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import csv

count_green1=HSVConvertGreen.count_green
count_color1=HSVConvertDisease.count_color
csvData= [count_green1,count_color1]


with open('test.csv', 'w') as csvFile:
    writer = csv.writer(csvFile,dialect='excel')
    writer.writerow(csvData)

csvFile.close()
