import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#data = pd.read_csv('C:/Users/Yan/Desktop/Scripting/data_sets/suicide-rates-overview-1985-to-2016/master.csv')
data = pd.read_csv('C:/Users/Yan/Desktop/Scripting/data_sets/house_pricing/melb_data.csv/melb_data.csv')


print(data.head())

#print(data.shape)
print(data.columns)


#sns.pairplot(data, x_vars=['age'], y_vars=['suicides_no'])
sns.pairplot(data, x_vars=['Landsize','Rooms'], y_vars=['Price'], height=7, aspect=0.7, kind='reg')

plt.show()


### Linear regression

from sklearn.cross_validation import train_test_split
#change this line after, new syntax
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=1)

linreg = LinearRegression()
linreg.fit(x_train,y_train)

## Predicting with RMSE

import numpy as np 

y_pred = linreg.predict(X_test)
print(np.sqrt(metrics.mean_squared.error(y_test,y_pred)))



