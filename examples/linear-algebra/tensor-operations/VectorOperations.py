# NumPy's basic data structure is an indexable, 
# n-dimensional array containing elements of the same type (dtype). 
# Right away, you may notice we have overloaded the term 'dimension'. 
# Above, it was the number of elements in the vector, here, dimension 
# refers to the number of indexes of an array. A one-dimensional or 1-D 
# array has one index. In Course 1, we will represent vectors as NumPy 1-D arrays.

import numpy as np
import time

print("VECTOR CREATION")
print("")
print("")
# Data creation routines in NumPy will generally have a first 
# parameter which is the shape of the object. This can either be a single 
# value for a 1-D result or a tuple (n,m,...) specifying the shape 
# of the result. Below are examples of creating vectors using these routines.

print("--NumPy routines which allocate memory and fill arrays with value")
a = np.zeros(4);                print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.zeros((4,));             print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.random_sample(4); print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
print("")


print("--Some data creation routines do not take a shape tuple:")

# NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument
a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
print("")

print("--values can be specified manually as well.")

a = np.array([5,4,3,2]);  print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}")
a = np.array([5.,4,3,2]); print(f"np.array([5.,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
# These have all created a one-dimensional vector a with four elements. 
# a.shape returns the dimensions. Here we see a.shape = (4,) indicating 
# a 1-d array with 4 elements.
print("")


print("INDEXING")
print("")
print("")
# Indexing means referring to an element of an array by its position within the array.
# Slicing means getting a subset of elements from an array based on their indices.
# NumPy starts indexing at zero so the 3rd element of an vector  𝐚
#   is a[2].

print("--vector indexing operations on 1-D vectors")
a = np.arange(10)
print(a)
print("")

print("--access an element")
print(f"a[2].shape: {a[2].shape} a[2]  = {a[2]}, Accessing an element returns a scalar")
print("")

print("--access the last element, negative indexes count from the end")
print(f"a[-1] = {a[-1]}")
print("")

print("--indexes must be within the range of the vector or they will produce and error")
try:
    c = a[10]
except Exception as e:
    print("The error message you'll see is:")
    print(e)
    
print("")

print("SLICING")
print("")
print("")

# Slicing creates an array of indices using a set of 
# three values (start:stop:step). A subset of values is 
# also valid. Its use is best explained by example:

print("--vector slicing operations")
a = np.arange(10)
print(f"a         = {a}")
print("")

print("--access 5 consecutive elements (start:stop:step)")
c = a[2:7:1];     print("a[2:7:1] = ", c)
print("")

print("--access 3 elements separated by two ")
c = a[2:7:2];     print("a[2:7:2] = ", c)
print("")

print("--access all elements index 3 and above")
c = a[3:];        print("a[3:]    = ", c)
print("")

print("--access all elements below index 3")
c = a[:3];        print("a[:3]    = ", c)
print("")

print("--access all elements")
c = a[:];         print("a[:]     = ", c)
print("")