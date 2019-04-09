# Converting text values to np arrays

import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=)


