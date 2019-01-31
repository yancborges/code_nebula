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










