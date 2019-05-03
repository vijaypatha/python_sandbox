#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
#create a dictionary 
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}
#turning the dictionary into dataframe
df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2'])
df1


# In[3]:

#create a dictionary 
dummy_data2 = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}
#turning the dictionary into dataframe
df2 = pd.DataFrame(dummy_data2, columns = ['id', 'Feature1', 'Feature2'])
df2


# In[4]:


dummy_data3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}
#create a dictionary 
df3 = pd.DataFrame(dummy_data3, columns = ['id', 'Feature3'])

df3


# In[5]:

#Concatnating two dataframes
df_row = pd.concat([df1, df2])

df_row


# In[6]:


df_merge_col = pd.merge(df_row, df3, on='id')

df_merge_col


# In[ ]:




