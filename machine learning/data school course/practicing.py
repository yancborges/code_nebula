#### Applying what i've learned so far

import imp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Loading data
data = pd.read_csv('C:/Users/Yan/Desktop/Scripting/data_sets/heart-disease-uci/heart.csv')

# Checking it
print(data.columns)
print(data.head())
print(data.shape)

## Splitting data
X = data.loc[:,:'thal']
y = data.loc[:,'target']
print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

## Training
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

## Predicting
y_pred = logreg.predict(X_test)

## Validating
print(metrics.accuracy_score(y_test,y_pred))




