# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:47:00 2026

@author: Jagatjyoti
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r'C:\Users\Jagatjyoti\Jagat_Code\02-05-2026\Data.csv')

# dataset2 = pd.read_csv('C:\\Users\\Jagatjyoti\\Jagat_Code\\02-05-2026\\Data.csv')
x = dataset.iloc[:, :-1].values
# DEPENDENT VARIABLE
y = dataset.iloc[:, -1].values

from sklearn.impute import SimpleImputer
# imputer = SimpleImputer()
# imputer = SimpleImputer(strategy='median')
imputer = SimpleImputer(strategy= 'most_frequent')
imputer = imputer.fit(x[:,1:3])

x[:,1:3] = imputer.transform(x[:,1:3])

from sklearn.preprocessing import LabelEncoder

lableencoder_x = LabelEncoder()
x[:,0]= lableencoder_x.fit_transform(x[:,0])

lableencoder_y = LabelEncoder()
y= lableencoder_y.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8, test_size= 0.2, random_state=0)
