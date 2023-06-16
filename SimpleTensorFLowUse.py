# By Ricardo Nader - 06102023

# -->PyTorch and TensorFlow are the two most popular automatic differentiation libraries (a focus of the Calculus I and Calculus II subjects 
# in the ML Foundations series) in Python, itself the most popular programming language in ML

# -->PyTorch tensors are designed to be pythonic, to feel and behave like NumPy arrays
# -->The advantage of PyTorch tensors relative to NumPy arrays is that they easily be used for operations on GPU
# -->Documentation on PyTorch tensors, including available data types

import torch


print("- Creating a basic int scalar")
x_pt = torch.tensor(25)
print("")

print("- current value of the tensor")
print(x_pt)
print("")

print("- Outputing its shape")
x_pt.shape
print(x_pt.shape)
print("")






