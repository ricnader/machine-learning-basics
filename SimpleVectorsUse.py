# By Ricardo Nader - 06102023

# Vectors (Rank 1 Tensors) in NumPy

import numpy as np


print("- Defining array/vector")
# type argument is optional, e.g.: dtype=np.float16
x = np.array([25,2,5])
print(x)
print("")


print("- Outputing length")
print(len(x))
print("")

print("- Outputing shape")
print(x.shape)
print("")

print("- Outputing type")
print(type(x))
print("")

print("- Outputing element of the array/vector")
print(x[0])
print("")

print("- Outputing the type of the element")
print(type(x[0]))
print("")
