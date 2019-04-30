#!/usr/bin/env python
# coding: utf-8

# In[3]:


# We import Pandas as pd into Python
import pandas as pd

# We create a dictionary of Pandas Series 
items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

# We print the type of items to see that it is a dictionary
print(items)
print(type(items))


# In[5]:


shopping_carts = pd.DataFrame(items)
shopping_carts


# In[7]:


# We create a dictionary of Pandas Series 
people = [{'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}]
store_items = pd.DataFrame(people, index = ['store 1', 'store 2'])
store_items


# In[10]:


import pandas as pd
import numpy as np

# Since we will be working with ratings, we will set the precision of our 
# dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame. 

# Create a dictionary with the data given above
dat = {'Book Title' : books,
       'Author' : authors,
       'User 1' : user_1,
       'User 2' : user_2,
       'User 3' : user_3,
       'User 4' : user_4}
#print('dat:')
#print(dat)
# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)
book_ratings

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:

book_ratings.fillna(book_ratings.mean(), inplace = True)



# In[10]:


import pandas as pd

# pandas series 
books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland'], index = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll'])
#authors = pd.Series(data = [], index = [])

# lets create a dictionary of panda series 
books_list = {'bookNames': pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland'], index = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll']),
              'TotalBooks': pd.Series(data = [1,2,3,4,5], index = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll'])}
books_list
print(type(books_list))


# In[12]:


library = pd.DataFrame(books_list)
library


# In[18]:


import pandas as pd
import numpy as np

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame. 

# Create a dictionary with the data given above
dat = {'Book Title' : books,
       'Author' : authors,
       'User 1' : user_1,
       'User 2' : user_2,
       'User 3' : user_3,
       'User 4' : user_4}

print(dat)
print(type(dat))
# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)
book_ratings


# In[21]:


print("DF book_ratings")
book_ratings


# In[24]:


#Accessing a value based on the colum row
print(book_ratings['Author' ][2])


# In[28]:


#Accessing the columns
print(book_ratings[['Author','User 4']])


# In[31]:


print(book_ratings.loc[[0]])


# In[32]:


User5 = book_ratings['User 1'] + book_ratings['User 2'] 
User5


# In[34]:


User6 = User5.fillna(0)
User6


# In[ ]:




