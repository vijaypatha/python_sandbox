#slicing based on the known index 
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
#Step 1 Create a array
x = np.arange(5,105,5).reshape(4,5)
print(x)


# In[5]:


#Step 2:Slice the array because i know the indices of the arrays. 
print("Original array")
print(x)

y = x[0:3, 0:3]
print("Sliced Array")
print(y)


# In[20]:


z = x[2:5,0:2]
print(z)


# In[22]:


w = x[:,3:5]
print(w)


# In[26]:


# If we modify a slice, it impacts the original array 
print("orignal array X")
print(x)
print("original W, a subset of X, w = x[:,3:5]")
print(w)
w[0,1] = 666 #target 25 to modify it to 666
print("modified W, changing 25 to 666")
print(w) 

print("modifited array X")


# In[27]:


x = np.arange(5,105,5).reshape(4,5)
print(x)


# In[29]:


y = x[0:3, 0:3].copy()
print(y)
y[0,1] = 888
print(y)
print(x)


# In[ ]:




