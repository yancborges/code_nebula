import pandas as pd 

### Rename

ufo = pd.read_csv('http://bit.ly/uforeports')

ufo.columns
# Returns a list with all column names

ufo.rename(columns = {'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
# Looks for the first argument in columns, and rename for the second argument
# inplace = If true returns a new dataframe, not a copy

ufo_cols = ['city','colors reported','shape reported','state','time']
ufo.columns = ufo_cols
# Overwrittes the name of the dataframe columns with the values in the list

ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols, header=0)
# Reads the file with that list as header name
# header = 0: The file does contain a row with header name. This argument ignores it

### Removing

ufo.drop('Colors Reported', axis=1, inplace=True)
# Removes that column

ufo.drop([0,1], axis=0, inplace=True)
# Drops the first two rows


