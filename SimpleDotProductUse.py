# By Ricardo Nader - 16062023

# If we have two vectors (say, x and y) with the same length n, we can calculate the dot product between them. This is annotated several different ways, including the following:

# x⋅y 
# xTy 
# ⟨x,y⟩


# Regardless which notation you use (I prefer the first), the calculation is
# the same; we calculate products in an element-wise fashion and then sum reductively across the 
# products to a scalar value. That is,  x⋅y = ∑ni = 1xiyi 

# The dot product is ubiquitous in deep learning: It is performed at every artificial neuron
# in a deep neural network, which may be made up of millions 
# (or orders of magnitude more) of these neurons.


import torch
import numpy as np

print("- Defining arrays/vectors")
# type argument is optional, e.g.: dtype=np.float16
x = np.array([25,2,5])
y = np.array([41,85,2])
print(x)
print(y)
print("")

print("- Calculating dot product manually")
print("25*41 + 85*2 + 5*2 = ",25*41 + 85*2 + 5*2)
print("")

print("- Calculating dot product with numPy")
print("np.dot(x,y) :",np.dot(x,y))
print("")

print("- Declaring tensors for torch")
x_pt = torch.tensor([25,2,5])
y_pt = torch.tensor([41,85,2])
print("")

print("- We can even calculate torch tensors with numPy:")
print("np.dot(x_pt,y_pt) = ",np.dot(x_pt,y_pt))
print("")

print("- Calculating with torch")
print("torch.dot(x_pt,y_pt) = ",torch.dot(x_pt,y_pt) )
print("")


print("np.dot(x,y) :",np.dot(x,y))
print("")
