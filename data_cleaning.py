'''
Source = https://realpython.com/python-data-cleaning-numpy-pandas/
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
#at index 1905 and onwards, give me the values of the column Date of Publication. 
df.loc[1905:, 'Date of Publication'].head(10)
'''
A particular book can have only one date of publication. Therefore, we need to do the following:

Remove the extra dates in square brackets, wherever present: 1879 [1878]
Convert date ranges to their “start date”, wherever present: 1860-63; 1839, 38-54
Completely remove the dates we are not certain about and replace them with NumPy’s NaN: [1897?]
Convert the string nan to NumPy’s NaN value
'''

'''
we can actually take advantage of a single regular expression to extract the publication year:

regex = r'^(\d{4})'

The regular expression above is meant to find any four digits at the beginning of a string, which suffices for our case. 
The above is a raw string (meaning that a backslash is no longer an escape character), which is standard practice with regular expressions.

The \d represents any digit, and {4} repeats this rule four times. 
The ^ character matches the start of a string, and the parentheses denote a capturing group, which signals to Pandas that we want to extract that part of the regex. 
(We want ^ to avoid cases where [ starts off the string.)
'''
extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
extr.loc[1905:,].head(20)
extr.head(10)

df['Date of Publication'] = pd.to_numeric(extr)