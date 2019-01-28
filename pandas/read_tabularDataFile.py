import pandas as pd 

# Getting data from web
orders = pd.read_table('http://bit.ly/chiporders')

# Getting data from web
user_cols = ['user_id','age','gender','occupation','zip_code']
pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)

# Sep = Separator, by default pandas uses a tab as separator
# Names = Names of columns, takes a list of strings as argument
# Skip_rows = Ignore rows at top
# Skip_footer = Ignore rows at bottom

