import pandas as pd 

# Getting data from web
ufo = pd.read_csv('http://bit.ly/uforeports')

# read_csv makes the default separator character as ',' instead of tabs

ufo['City']

# Getting all values from the requested column
# The output is a panda series

ufo.City

# Each time a series is added to this objetct,
# pandas auto creates an attribute with that name

# Doesnt work with spaced names, like 'Colors reported'

ufo.shape

# shows the dimension of that list (a x b size ex.)

ufo.City + ufo.State
ufo.City + ',' + ufo.State
ufo['Location'] = ufo.City + ',' + ufo.State

# Concatenates two panda series into a new one
# Doesnt work (the new one) with atributes, requires brackets

print(ufo)

