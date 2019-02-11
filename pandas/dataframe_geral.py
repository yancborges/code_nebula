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



















