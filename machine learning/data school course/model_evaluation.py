import imp
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.preprocessing import binarizer
from sklearn.cross_validation import cross_val_score

### Modeling

col_names = ['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/scikit-learn-videos/master/data/pima-indians-diabetes.data', header=None, names=col_names)

feature_cols = ['pregnant','insulin','bmi','age']
X = data[feature_cols]
y = data.label

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print(metrics.accuracy_score(y_test, y_pred))


### The confusion matrix

print(confusion_matrix(y_test, y_pred))

confusion = metrics.confusion_matrix(y_test, y_pred)
TP = confusion[1,1]
TN = confusion[0,0]
FP = confusion[0,1]
FN = confusion[1,0]


# Missclassification rate
print(1 - metrics.accuracy_score(y_test, y_pred))

# Sensitivity metric
print(metrics.recall_score(y_test, y_pred))

# Specifity metric
print(TN/ float(TN + TP))

# False positive rate
print(FP/ float(TN + FP))

# Precision score
print(metrics.precision_score(y_test, y_pred))


### Adjusting the classification threshold

y_pred_proba = logreg.predict_proba(X_test)[:,1]
print(y_pred_proba)

# Plotting

plt.rcParams['font.size'] = 14

plt.hist(y_pred_proba, bins=0)
plt.xlim(0,1)
plt.title('Look at this graAAaaAph')
plt.xlabel('Predicted probability of diabetes')
plt.ylabel('Frequency')

# Preprocessing

y_pred = binarizer(y_pred_proba, 0.3)[0]


### ROC curves and area under the curve

fpr, tpr thresholds = metrics.roc_curve(y_test, y_pred_proba)

plt.plot(fpr,tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.title('Every time I do it makes me laugh ')

def evaluate_threshold(threshhold):
	print('Sensitivity: %s', %tpr[thresholds > threshhold][-1])
	print('Sensibility: %s' %fpr[threshholds > threshhold][-1])


# Getting auc

print(metrics.roc_auc_score(y_test, y_pred_proba))

# Cross val score

cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean()





















