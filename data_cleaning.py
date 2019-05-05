'''
We’ll cover the following:

Dropping unnecessary columns in a DataFrame
Changing the index of a DataFrame
Using .str() methods to clean columns
Using the DataFrame.applymap() function to clean the entire dataset, element-wise
Renaming columns to a more recognizable set of labels
Skipping unnecessary rows in a CSV file
'''
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/vipatha/Documents/python_sandbox/BL-Flickr-Images-Book.csv')
df.head()
#Dropping unnecessary columns in a DataFrame
to_drop = ['Edition Statement','Corporate Author','Corporate Contributors','Former owner','Engraver','Contributors','Issuance type','Shelfmarks']
df.drop(columns = to_drop, inplace=True)
df.head()
#Checking for unique values in a column
df['Identifier'].is_unique
df.head()
#Changing the index of a DataFrame

df.set_index('Identifier', inplace=True)

'''
Technical Detail: Unlike primary keys in SQL, a Pandas Index doesn’t make any guarantee of being unique, 
although many indexing and merging operations will notice a speedup in runtime if it is.
'''
df.get_dtype_counts()
df.dtypes
df.loc[1905:, 'Date of Publication'].head(10)