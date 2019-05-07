#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
TODO: Multiply Vector by Scalar and Plot Results
For this part of the lab you will be creating vector $\vec{av}$ and then adding to the plot as a dotted cyan colored vector.

Multiply vector $\vec{v}$ by scalar $a$ in the code below (see TODO 1.:).
 

Use the ax.arrow(...) statement in the code below to add vector $\vec{av}$ to the plot (see *TODO 2.:). 
Adding linestyle = 'dotted' and changing color = 'c' in the ax.arrow(...) 
statement will make vector $\vec{av}$ a dotted cyan colored vector.

'''

# Import NumPy and Matplotlib **Only needed for running code in solutions notebook**
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

# Define vector v 
v = np.array([1,1])

# Define scalar a
a = 3

# DONE 1.: Define vector av - as vector v multiplied by scalar a
av = a*v

# Plots vector v as blue arrow with red dot at origin (0,0) using Matplotlib

# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0,0,'or')

# Plots vector v as blue arrow starting at origin 0,0
ax.arrow(0, 0, *v, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)

# DONE 2.: Plot vector av as dotted (linestyle='dotted') vector of cyan color (color='c') 
# using ax.arrow() statement above as template for the plot 
ax.arrow(0, 0, *av, color='c', linestyle='dotted', linewidth=2.5, head_width=0.30, 
         head_length=0.35)


# Sets limit for plot for x-axis
plt.xlim(-2, 4)

# Set major ticks for x-axis
major_xticks = np.arange(-2, 4)
ax.set_xticks(major_xticks)


# Sets limit for plot for y-axis
plt.ylim(-1, 4)

# Set major ticks for y-axis
major_yticks = np.arange(-1, 4)
ax.set_yticks(major_yticks)

# Creates gridlines for only major tick marks
plt.grid(b=True, which='major')

# Displays final plot
plt.show()


# In[2]:


'''
TODO: Adding Two Vectors and Plotting Results
For this part of the lab you will be creating vector $\vec{vw}$ and then adding it to the plot as a thicker width black colored vector.

Create vector $\vec{vw}$ by adding vector $\vec{w}$ to vector $\vec{v}$ in the code below (see TODO 1.:).
 

Use the ax.arrow(...) statement in the code below to add vector $\vec{vw}$ to the plot (see *TODO 2.:). 

Changing linewidth = 3.5 and color = 'k' in the ax.arrow(...) statement will make vector $\vec{vw}$ a 

thicker width black colored vector.
'''


# In[3]:


# Define vector v 
v = np.array([1,1])

# Define vector w
w = np.array([-2,2])

# DONE 1.: Define vector vw by adding vectors v and w 
vw = v + w

# Plot that graphically shows vector vw (color='b') - which is the result of 
# adding vector w(dotted cyan arrow) to vector v(blue arrow) using Matplotlib

# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0,0,'or')

# Plots vector v as blue arrow starting at origin 0,0
ax.arrow(0, 0, *v, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)

# Plots vector w as cyan arrow with origin defined by vector v
ax.arrow(v[0], v[1], *w, linestyle='dotted', color='c', linewidth=2.5, 
         head_width=0.30, head_length=0.35)

# DONE 2.: Plot vector vw as black arrow (color='k') with 3.5 linewidth (linewidth=3.5)
# starting vector v's origin (0,0)
ax.arrow(0, 0, *vw, color='k', linewidth=3.5, head_width=0.30, head_length=0.35)


# Sets limit for plot for x-axis
plt.xlim(-3, 2)

# Set major ticks for x-axis
major_xticks = np.arange(-3, 2)
ax.set_xticks(major_xticks)


# Sets limit for plot for y-axis
plt.ylim(-1, 4)

# Set major ticks for y-axis
major_yticks = np.arange(-1, 4)
ax.set_yticks(major_yticks)

# Creates gridlines for only major tick marks
plt.grid(b=True, which='major')

# Displays final plot
plt.show()


# In[ ]:




