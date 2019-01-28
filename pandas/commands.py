import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

movies.head()
# First five rows of the dataframe

movies.descibe()
# Statistic form numeric columns

movies.shape
# Shows the dimension of the df

movies.dtypes
# Returns the type of each column

