import imp
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)

#knn.predict([3,5,4,2])

X_new = [[3,5,4,2],[5,4,3,2]]
knn.predict(X_new)

###

from sklearn.linear_model import LogisticRegression

log = LogisticRegression()

log.fit(X,y)
log.predict(X_new)

###

logreg = LogisticRegression()
logreg.fit(X,y)
logreg.predict(X)

y_pred = logreg.predict(X)

from sklearn import metrics

print(metrics.accuracy_score(y,y_pred))

####

##### SPLIT THE DATA INTO TRAINING, AND TEST DATA
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

##### TRAIN MODEL WITH THE SPLITTED TRAINING DATA
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

##### MAKE PREDICTIONS ON THE TEST SET
y_pred = logreg.predict(X_test)

##### GET ACCURACY
print(metrics.accuracy_score(y_test,y_pred))

## Getting the best value for K (in knn)

k_range = range(1,26)
scores = []
for k in k_range:
	knn = KNeighborsClassifier(n_neighbors=k)
	knn.fit(X_train, y_train)
	y_pred = knn.predict(X_test)
	scores.append(metrics.accuracy_score(y_test,y_pred))

## Plotting

import matplotlib.pyplot as plt 

#%matplotlib inline

plt.plot(k_range, scores)
plt.xlabel('Value o K')
plt.ylabel('Testing accuracy')
plt.show()

### Out of sample prediction

knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X,y)

print(knn.predict([[3,5,4,2]]))
