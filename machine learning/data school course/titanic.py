import pandas as pd
import numpy as np
import random as rnd
import imp

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data_train = pd.read_csv('C:/Users/Yan/Desktop/Scripting/data_sets/titanic/train.csv')
data_test = pd.read_csv('C:/Users/Yan/Desktop/Scripting/data_sets/titanic/test.csv')

print(data_train[['Sex','Survived']].groupby(['Sex']).mean().sort_values(by='Survived', ascending=False))

g = sns.FacetGrid(data_train, col='Survived')
g.map(plt.hist, 'Age', bins=20)
plt.show()

X_train = data_train.drop('Survived', axis=1)
y_train = data_train['Survived']
X_test = data_test.drop('PassengerId', axis=1)

# Values here must be changed all to numeric, and field like name may be dropped

### Logistic regression

logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred = logreg.predict(X_test)

score = metrics.accuracy_score(y_test,y_pred)
print(score)



