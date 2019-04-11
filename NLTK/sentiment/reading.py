import imp
from nltk.sentiment import sentiment_analyzer
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

data = pd.read_json('C:/Users/Yan/Desktop/Scripting/data_sets/news-headlines-dataset-for-sarcasm-detection/Sarcasm_Headlines_Dataset.json', lines=True)

X = data.headline
y = data.is_sarcastic

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

vect = CountVectorizer(stop_words='english')
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)

forest = RandomForestClassifier(n_estimators=100)
forest.fit(X_train_dtm, y_train)

y_pred = forest.predict(X_test_dtm)
print(metrics.accuracy_score(y_test,y_pred))




