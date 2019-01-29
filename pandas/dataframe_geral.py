import pandas as pd 

movies = pd.read_csv('http://bit.ly/imdbratings')

### Filtering

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

