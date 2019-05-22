import imp
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.preprocessing import binarize
from sklearn.model_selection import cross_val_score

def toFloat(matrix):
	new_matrix = []
	for array in matrix:
		new_array = []
		for item in array:
			if(str(item) in '01'):
				new_array.append(float(item))
		new_matrix.append(new_array)
	return new_matrix

def binary_string_gen(non_binary):
		binary_array = []
		for i in range(1,MAX_GENRES):
			if(i in non_binary):
				binary_array.append(1)
			else:
				binary_array.append(0)
		return binary_array

nick ='ThousandAntas'
MAX_GENRES = 43

data = pd.read_csv(nick + '_ds.csv', sep='=@', engine='python')

X = toFloat(list(data.Genres_id))
y = data.Score

X_train, X_test, y_train, y_test = train_test_split(X, y)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print(metrics.accuracy_score(y_test, y_pred))
print(metrics.confusion_matrix(y_test, y_pred))

y_pred_proba = logreg.predict_proba(X_test)
print(y_pred_proba)

y_pred = binarize(y_pred_proba, 0.7)
print(y_pred)

print(logreg.predict_proba([binary_string_gen([[1,14,40,37,8,22,42]])]))
