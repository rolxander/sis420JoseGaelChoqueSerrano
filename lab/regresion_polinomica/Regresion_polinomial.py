# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:34:08 2019

@author: MPC
"""

from sklearn import datasets
dataset = datasets.load_breast_cancer()

X = dataset.data
y = dataset.target
from sklearn.model_selection import train_test_split
X_train , X_test, y_train,y_test = train_test_split(X,y,test_size=0.2)
from sklearn.preprocessing import StandardScaler
escalar = StandardScaler()
X_train = escalar.fit_transform(X_train)
X_test = escalar.transform(X_test)
from sklearn.linear_model import LogisticRegression
algoritmo = LogisticRegression()
algoritmo.fit(X_train,y_train)
y_pred = algoritmo.predict(X_test)
#from sklearn.metrics import confusion_matrix
#matriz = confusion_matrix(y_test,y_pred)
from sklearn.metrics import precision_score
presicion = precision_score(y_test,y_pred)
print("La presicion es de ")
print(presicion)

