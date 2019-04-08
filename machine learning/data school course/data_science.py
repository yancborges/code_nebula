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

