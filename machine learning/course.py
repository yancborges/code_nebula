### ================== Data exploration

import pandas as pd 

melb = pd.read_csv('melb_data.csv')
#print(melb.describe())
print(melb.columns)
melb = melb.dropna(axis=0)


