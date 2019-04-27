'''
What is numpy?

NumPy stands for Numerical Python and it's a fundamental package for scientific computing in Python. NumPy provides Python with an extensive math library capable of performing numerical computations effectively and efficiently. 

Why numpy?
Even though Python lists are great on their own, NumPy has a number of key features that give it great advantages over Python lists.
1) Speed
2) multidimensional array data structures that can represent vectors and matrices.(a lot of machine learning algorithms rely on matrix operations.)
3) Another great advantage of NumPy over Python lists is that NumPy has a large number of optimized built-in mathematical functions.


The Basics
NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In NumPy dimensions are called axes. The number of axes is rank.

For example, the coordinates of a point in 3D space [1, 2, 1] is an array of rank 1, because it has one axis. That axis has a length of 3. In the example pictured below, the array has rank 2 (it is 2-dimensional). The first dimension (axis) has a length of 2, the second dimension has a length of 3.






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

The more important attributes of an ndarray object are:

ndarray.ndim
the number of axes (dimensions) of the array. In the Python world, the number of dimensions is referred to as rank.

ndarray.shape
the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the rank, or number of dimensions, ndim.

ndarray.size
the total number of elements of the array. This is equal to the product of the elements of shape.

ndarray.dtype
an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

ndarray.itemsize
the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to 
ndarray.dtype.itemsize.

ndarray.data
the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.


'''

import numpy as np
x = np.array([1,2,3,4,5])
print('x =', x)

'''
np.array() function that produces ndarrays

What is the shape of the array -> x.shape
What is type of dimmenions in array -> x.dtype
what is the object type of x -> type(x)
'''

print(x.shape)
print(x.dtype)
print(type(x))

np.save("myArray", x)
y = np.load('myArray.npy')


'''
One great time-saving feature of NumPy is its ability to create ndarrays using built-in functions. These functions allow us to create certain kinds of ndarrays with just one line of code. Below we will see a few of the most useful built-in functions for creating ndarrays that you will come across when doing AI programming.


How to create ndarrays with specific SHAPES:


'''