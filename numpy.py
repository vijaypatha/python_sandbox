'''
What is numpy?

NumPy stands for Numerical Python and it's a fundamental package for scientific computing in Python. NumPy provides Python with an extensive math library capable of performing numerical computations effectively and efficiently. 

Why numpy?
Even though Python lists are great on their own, NumPy has a number of key features that give it great advantages over Python lists.
1) Speed
2) multidimensional array data structures that can represent vectors and matrices.(a lot of machine learning algorithms rely on matrix operations.)
3) Another great advantage of NumPy over Python lists is that NumPy has a large number of optimized built-in mathematical functions.

What is multidimensional array data structure? 
At the core of NumPy is* the ndarray, where nd stands for n-dimensional. An ndarray is a multidimensional array of elements all of the same type. 

**** What is ndarray? ***
In other words, an ndarray is a grid that can take on many shapes and can hold either numbers or strings. In many Machine Learning problems you will often find yourself using ndarrays in many different ways. For instance, you might use an ndarray to hold the pixel values of an image that will be fed into a Neural Network for image classification.

*** How to create ndarray ***
There are many ways to do it:
1) Using regular python lists
2) using built-in numpy functions


 providing Python lists to the NumPy np.array() function. This can create some confusion for beginners, but it is important to remember that np.array() is NOT a class, it is just a function that returns an ndarray. We should note that for the purposes of clarity, the examples throughout these lessons will use small and simple ndarrays

What is np.array() -> its a function in numpy that returns ndarray


'''
'''
import sys

print(sys.version)
'''
import numpy as np
x = np.array([1,2,3,4,5])
print('x =', x)
