import pandas as pd 
import imp
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

# Getting the labeled data
data = pd.read_json('C:/Users/Yan/Desktop/Scripting/data_sets/news-headlines-dataset-for-sarcasm-detection/Sarcasm_Headlines_Dataset.json', lines=True)

# Checking labels
print(data.columns)

# Splitting values
X = data.headline 
y = data.is_sarcastic

# Selecting 40% of set for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# Ignoring stop words
vect = CountVectorizer(stop_words='english')
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)

# Instancing logistic regression
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)

# Predicting
y_pred = logreg.predict(X_test_dtm)

# Getting accuracy of the test
print(metrics.accuracy_score(y_test, y_pred))

# Making a prediction from input!
line = [input('Headline: ')]
line_dtm = vect.transform(line)
new_y_pred = logreg.predict(line_dtm)
if(new_y_pred == 0):
	print('No sarcasm')
else:
	print('Sarcasm detected!')

