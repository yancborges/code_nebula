# Converting text values to np arrays

import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import LogisticRegression

simple_train = ['call you tonight','call me a cab','please call me.... PLEASE']

vect = CountVectorizer()
vect.fit(simple_train)

vect.get_feature_names()

simple_train_dtm = vect.transform(simple_train)
simple_train_dtm.toarray()

pd.DataFrame(simple_train_dtm.toarray(), columns=vect.get_feature_names())

simple_test = ["please don't call me"]
simple_test_dtm = vect.transform(simple_test)
simple_test_dtm.toarray()



sms = pd.read_table('https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv', header=None, name=['label', 'message'])
print(sms.label.value_counts())

X = sms.message
y = sms.label_num

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

vect = CountVectorizer()

vect.fit(X_train)
X_train_dtm = vect.transform(X_train)

# OR: X_train_dtm = vect.fit_transform(X_train)

X_test_dtm = vect.fit_transform(X_test)



nb = MultinomialNB()

nb.fit(X_train_dtm, y_train)

y_pred_class = nb.predict(X_test_dtm)
print(metrics.accuracy_score(y_test,y_pred_class))
print(metrics.confusion_matrix(y_test, y_pred_class))

# Priting false positives(spam)
print(X_test[(y_pred_class==1) & (y_test==0)])
print(X_test[y_pred_class > y_test])

# Priting false negatives(ham)
print(X_test[y_pred_class < y_test])

# Probab % of being spam (index 1)
y_pred_prob = nb.predict_proba(X_test_dtm)[:,1]

print(metrics.roc_auc_score(y_test, y_pred_prob))



logreg = LogisticRegression()

logreg.fit(X_train_dtm, y_train)
y_pred_prob_class = logreg.predict(X_test_dtm)

y_pred_prob = logreg.predict_proba(X_test_dtm)[:,1]

print(metrics.accuracy_score(y_test, y_pred_class))
print(metrics.roc_auc_score(y_test, y_pred_prob))



X_train_tokens = vect.get_feature_names()

nb.feature_count_.shape

ham_token_count = nb.feature_count_[0,:]
print(ham_token_count)

tokens = pd.DataFrame({'token':X_train_tokens, 'ham':ham_token_count, 'spam':spam_token_count}).set_index('token')
print(tokens.head())

print(nb.class_count_)



vect = CountVectorizer(stop_words='english')
vect = CountVectorizer(ngram_range=(1,2))
vect = CountVectorizer(max_df=0.5)
vect = CountVectorizer(min_df=2)


























