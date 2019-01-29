import pandas as pd 

movies = pd.read_csv('http://bit.ly/imdbratings')

movies.title.sort_values()
movies['title'].sort_values()
# Sort all titles, retuned as a panda series

movies.titles.sort_values(ascending=False)
# Inverted, sorted by desc

movies.sort_values('titles')
# Request sorting by a column
# This sorts all the dataframe based on the column in parameter

movies.sort_values(['content_rating', 'duration'])
# Sorted first by content rating, then by duration

