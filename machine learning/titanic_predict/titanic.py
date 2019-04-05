import pandas as pd 
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('http://bit.ly/kaggletrain')
test = pd.read_csv('http://bit.ly/kaggletest')
print(train.head())

## training

feats = ['Pclass','Parch']
x = train.loc[:,feats]
y = train.Survived

logreg = LogisticRegression()
logreg.fit(x,y)


## testing

x_new = test.loc[:,feats]
new_pred = logreg.preditc(x_new)
print(new_pred)


## model

pd.Dataframe({'PassengerId':test.PassengerId,'Survived':new_pred}).set_index('PassengerId').to_csv('model.csv')
