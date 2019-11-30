# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:02:48 2019

@author: MPC
"""

import pandas as pd
import numpy as np 
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
boston = datasets.load_boston()
#print(boston)
#print(boston.keys())
#print(boston.data.shape)
#print(boston.DESCR)
#print(boston.feature_names)
X_multiple=boston.data[:,5:8]#los datos toamdos de x necesito vectorizarlos para el vector
y_multiple = boston.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_multiple,y_multiple,test_size=0.2)
lr_multiple = linear_model.LinearRegression()
y_pred_multiple = lr_multiple.predict(X_test)






