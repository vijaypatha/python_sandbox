'''
pretty simple:
1) Create a array
2) Manipylate the arary: Accessing, deleting, inserting, slicing etc 
'''

#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np

#Step 1: Create a array
x = np.arange(5,55,5).reshape(2,5)

print("Array X is:")
print(x)

print("Attrubute of Array X is:")
print("# of axis of x: ", x.ndim)
print("# row and columns in X:", x.shape)
print("Data type of X:",x.dtype)
print("# of elements in the array X:", x.size)


# In[11]:


#Step 2: Access a element in the array 
x[1,3] #expecting 2 row, 4th colum element -> 45
print(x[1,3])


# In[12]:


#Step 3: Changing 45 to 95
x[1,3] = 95

print(x)


# In[13]:


#Step 4: Changing 95 to 45
x[1,3] = 45
print(x)


# In[32]:


#Step 5: delete something along Axis 1
print("array x is: ")
print(x)

y = np.delete(x,[1,3],1) # deleting array's index 1 and 3 along the axis 1 -> a columnwise opreation 
print("modified x after deleting index [0,4] along axis 1 is:")
print(y)


# In[33]:


#Step 5: delete something along Axis 1
print("array x is: ")
print(x)

z = np.delete(x,[0,4]) # deleting array's index 1 and 3 along the axis 0 -> a rowwise operation
print("modified x after deleting index [0,4] is",z)


# In[38]:


print("z = ", z)
t = np.delete(z, [0,2], axis=0)
print("modifed z =",t)


# In[45]:


# Step 6: Appending rows and columns 
print("y", y)
print("appended new column:")
print(np.append(y, [[55],[60]], axis = 1)) #notice the difference between appending a row vs. Column. 
#The new rows and columns match the shapes arrays


# In[49]:


print("y", y)
print("appended new row:")
print(np.append(y, [[55,60,65]], axis = 0)) #notice the difference between appending a row vs. Column. 
#The new rows and columns match the shapes arrays


# In[ ]:


# Step 7: Inserting rows and colummns np.insert(ndarray, index, elements, axis)
print("y array is",y)
w = np.insert(y, 2, [55,60,65],axis = 0)
print ("Inserted Y array is:")
print(w)



print("y array is")
print(y)
w = np.insert(y, 3, [[55],[60],[65]],axis = 1)
print ("Inserted Y array is:")
print(w)

# STep 8: Vstack and Hstack
print("y array is")
print(y)

w = np.hstack(y)
print ("hstacked Y array is:")
print(w)