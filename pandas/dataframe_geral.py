import pandas as pd 

movies = pd.read_csv('http://bit.ly/imdbratings')

### Filtering ###

bools = []
for mins in movies.duration
	if mins >= 200:
		bools.append(True)
	else:
		bools.append(False)

is_long = pd.Series(bools)
# Converting list to panda series

movies[is_long]
# Passing panda series to dataframe

is_long = movies.duration >= 200
# Does what for function does but in one line of code xD

movies[movies.duration >= 200]
# Does all the code above, but in one line of code

### Multiple filters

movies[(movies.duration >= 200) & (movies.genre == 'Drama')]
# Multiple filters requires () for each condition.
# also Or and And statements does not work here. Switch for & and |

### Tips ###

ufo = pd.read_csv('http://bit.ly/uforeports', usecols=[0,4])
# Reading only columns with index < 5

### Axis ###

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

drinks.drop('continent', axis=1)
# Dropping the 'continent' column

drinks.drop(2,axis=0)
# Dropping the 2 index of dataframe rows

## axis = 1 - Column
## axis = 0 - Row

drinks.mean()
# Shows the meadium value for each series in the dataframe
# default: axis=0 (index), axis = 1 (columns)

### String methods ###

orders = pd.read_table('http://bit.ly/chiporders')

orders.item_name.str.upper()
# Upper case item_name column values

orders.item_name.str.contains('Chiken')
# Returns a boolean list with based if there are the given argument in item_name column

### Converting ###

drinks['beer_servings'] = drinks.beer_servings.astype(float)
# Converts column values to float

drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
# Converting data type while its readed

### Group by ###

drinks.groupby('continent').beer_servings.mean()
# Appends all values from the same continent and calculates the mean value

drinks.groupby('continent').beer_servings.max()
# Shows the maximum value for each continent

drinks.groupby('continent').beer_servings.agg(['count','min','max','mean'])
# Appends all those commands and get values filtering by its continent

drinks.groupby('continent').mean()
# Returns the mean value for each column

%matplotlib inline
drinks.groupby('continent').mean().plot(kind='bar')
# Display graphics

### Exploring ###

movies.genre.value_counts()
# Returns the count of each value in the column

movies.genre.value_counts(normalize=True)
# % of occurance

movies.genre.unique()
# Return all unique values

### Missing values

ufo.isnull()
# Show for each value of each column if that value is missing or not (boolean)

ufo.notnull()
# Inverse of above

ufo.isnull().sum()
# Makes te sum of each PRESENT value, excluding Null values (in this case only 0 and 1 are summed)

ufo[ufo.City.isnull()].sum()
# Creates a series of trues and falses. Then pass it to the dataframe.
# So pandas appends both and show ONLY the rows where this city column is missing

ufo.dropna(how='any').shape
# Dropping all rows with any missing value

ufo.dropna(subset=['City','Shape Reported'], how='any')
# Dropping each row where City or Shape Reported columns are missing

ufo['Shape Reported'].value_counts(dropna=False)
# For default, pandas hides the missing values here
# This argument prevents that, so you can see how many are missing

ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
# Replaces all the missing values for this column with the gathered one

### INDEX ###

drinks.index
# Returns the indexes for that dataframe

drinks[drinks.continent=='South America']
# Shows all rows which the continent is 'South America'

drinks.loc[23,'beer_servings']
drinks.loc['Brazil','beer_servings'] # (only works after the command below)
# Returns the value from a cell matching row and column

drinks.set_index('country')
# Replaces indexes by row's country value

drinks.reset_index()
# Undo the command above

people = pd.Series([3000000, 850000], index=['Albania','Andorra'], names='population')
drinks.beer_servings * people
# Mutiplies both values. As we created a new series with only 2 itens,
# pandas will find those values in dataframe and make he math

pd.concat([drinks, people], axis=1)
# Concatenates a series to a dataframe

### Loc, iloc and ix ###

ufo.loc[0,:]
ufo.loc[[1,2,3],:]
ufo.loc[0:2,:]
ufo.loc[:,'City']
ufo.loc[:,['City', 'State']]
ufo.loc[:,'City':'State']
ufo.loc[ufo.City=='Oakland','State']
# Selecting things by labels

ufo.iloc[:,[0,3]]
# Selecting by interget position

drinks.ix['Albania',0]
drinks.ix[1,'beer_servings']
drinks.ix['Albania':'Andorra',0:2]
# Mixing labels and integets

# Labels are INCLUSIVE in both sides

### Category types ###

drinks['continent'] = drinks.continent.astype('category')
# Creates categories for each value in the series
# And then stores the values in dataframe by it's values id
# So all values are replaced by integers (making the size lighter)

df = pd.DataFrame({'ID':[100,101,102,103], 'quality':['good','very good','excellent']})
# Creating a series of values

df['quality'] = df.quality.astype('category', categories=['good','very good','excellent'], ordered=True)
# Creating a logical order for dataframe's values

df.loc[df.quality > 'good', :]
# Getting values only greater then 'good'
# Because now pandas undertands this kind of comparation

### Variables ###

train = pd.read_csv('http://bit.ly/kaggletrain')

train['Sex_male'] = train.Sex.map({'female':0,'male':1})
# Creating a new column with 0 and 1 (booleans) based if sex is male

pd.get_dummies(train.Sex, prefix='Sex').iloc[:,1:]
# Creates one column for each possible value in dataframe as the comand above

embarked = pd.get_dummies(train.Embarked, prefix='Embarked').iloc[:,1:]
# Some from above

pd.concat([train,embarked],axis=1)
# Appending dummy variables to dataframe

pd.get_dummies(train, columns=['Sex','Embarked'], drop_first=True)
# Creates dummy variables for the gathered columns

### Dates and time ###

ufo['Time'] = pd.to_dateTime(ufo.Time)
# Change the type of argument series to datetime

ufo.Time.dt.hour
# Returns all hours stored

ufo.Time.dt.weekday_name
# Returns the NAME of day

ts = pd.to_dateTime('1/1/1999')
# Ouputs a timestamp

ufo.loc[ufo.time >= ts,:]
# Return all days after the timestamp created previously

ufo.Time.max() - ufo.Time.min()
# Returns the result of this math as an object called timeDelta

### Duplicates ###

user_cols = ['user_id','age','gender','occupation','zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols index_col='user_id')

users.zip_code.duplicated()
# Return a series of booleans where True means that value is duplicated
# Only the second appear of the value is marked as a duplicate

users.duplicate()
# Tells if the whole row is duplicated somewhere

users.loc[users.duplicated(keep=False),:]
# Show only the duplicated rows

users.drop_duplicates(keep='first')
# Drops the duplicated rows

users.duplicated(subset=['age','zip_code'])
# Considers the gathered columns as relevant for being duplicates

### Display options ###

pd.get_option('display.max_rows')
# Returns the value of that option

pd.set_option('display.max_rows',None)
# Change the option value (in this case to None, that means all)

pd.reset_option('display.max_rows')
# Restores default options

pd.set_option('display.max_colwidth',1000)
# Width of columns. None isnt allowed here

pd.set_option('display.precision',2)
# At float, how many numbers after the comma will be displayed

### DataFrame handling ###

df = pd.DataFrame({'id':[100,101,102],'color':['red','blue','red']}, columns['id','color'], index=['a','b','c'])
# Creating a dataframe from zero

import numpy as np 
arr = np.random(4,2)
pd.DataFrame(arr,columns=['one','two'])
# Creatng an array with random numbers with numpy

pd.DataFrame({'student':np.arange(100,110,1),'test':np.random.randint(60,101,10)})
# ^^

s = pd.Series(['round','square'], index=['c','b'], name='shape')
pd.concat([df, s], axis=1)
# Appending the series to dataframe

### Apply, Map and ApplyMap ###

train['Sex_num'] = train.Sex.map({'female':0,'male':1})
train.loc[0:4,['Sex','Sex_num']]
# Translates female value to 0 and male value to 1

train['Name_length'] = train.Name.apply(len)
# Applying len function to name values

train['Fare_ceil'] = train.Fare.apply(np.ceil)
# Applying numpy function for rounding values up

deinks.loc[:,'beer_servings','wine_servings'].applymap(float)
# Applyies every cell with the argument method passed














































