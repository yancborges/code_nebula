import imp
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

house_ds = pd.read_csv('C:/Users/Yan/Desktop/Scripting/data_sets/house_pricing/melb_data.csv/melb_data.csv')

y = house_ds.Price
feats = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']
x = house_ds[feats]

#print(x.describe())

model = DecisionTreeRegressor(random_state=1)
model.fit(x,y)

print(house_ds.Price.head())
print(x.head())
print(model.predict(x.head())