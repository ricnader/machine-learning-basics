
import torch as tr
import tensorflow as tf

#with pyTorch
print("Using pyTorch")    
print("Defining x")
x = tr.tensor(2.0)

x.requires_grad_()

print("Defining y")
y = x**2 + 2*x + 2
y.backward()
print(x.grad)
print(x)



