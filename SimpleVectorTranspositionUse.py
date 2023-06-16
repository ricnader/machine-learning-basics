# By Ricardo Nader - 16062023

import torch
import numpy as np


print("- Defining array/vector")
# type argument is optional, e.g.: dtype=np.float16
x = np.array([25,2,5])
print(x)
print("")

print("- Transposing a regular 1-D array has no effect")
x_t = x.T
print(x_t)
print("")

print("- Shape of the vector x_t")
print(x_t.shape)
print("")

print("- but it does we use nested matrix-style brackets")
y = np.array([[25, 2, 5]])
print(y)
print("")

print("- Shape of the vector y")
print(y.shape)
print("")

print("- but can transpose a matrix with a dimension of length 1, which is mathematically equivalent")
y_t = y.T
print(y_t)
print("")

print("- Column vector can be transposed back to original row vector:")

print(y_t.T.shape)
print("")
