import imp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_json('C:/Users/Yan/Desktop/Scripting/data_sets/news-headlines-dataset-for-sarcasm-detection/Sarcasm_Headlines_Dataset.json', lines=True)
data.drop(columns=['article_link'], inplace=True)

X_train, X_test, y_train, y_test = train_test_split(data.headline,data.is_sarcastic,test_size=0.4)
vect = TfidfVectorizer()

scores = []
for i in range(6,14):
	model = DecisionTreeClassifier(max_depth=i)
	model.fit(vect.fit_transform(X_train),y_train)
	y_pred = model.predict(vect.transform(X_test))
	score = metrics.accuracy_score(y_test,y_pred)
	print('Accuracy score: ', score, ' Depth: ', i)
	scores.append(score)
print('Best score: ', max(scores) )

