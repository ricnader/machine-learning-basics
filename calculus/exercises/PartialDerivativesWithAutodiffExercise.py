
# Partial Derivatives of Multivariate Functions

# Define a function  f(x,y) for z=x2−y2 :


# Determine:

# x= 3, u= 0
# x= 2, u= 3
# x= -2, u= -3

import numpy as np
import matplotlib.pyplot as plt
import torch as tr
import math # for constant pi


#--------1
x = tr.tensor(3.).requires_grad_()
y = tr.tensor(0.).requires_grad_()

print("x: ",x)
print("y: ",y)

def f(my_x,my_y):
  return my_x**2 - my_y**2

z = f(x,y)

print(z.backward())

print("Solution 1")
print(x.grad)
print(y.grad)
print("")

#--------2

x = tr.tensor(2.).requires_grad_()
y = tr.tensor(3.).requires_grad_()

z = f(x,y)
z.backward()

print("Solution 2")
print(x.grad)
print(y.grad)
print("")

#--------3
x = tr.tensor(-2.).requires_grad_()
y = tr.tensor(-3.).requires_grad_()

z= f(x,y)
z.backward()

print("Solution 3")
print(x.grad)
print(y.grad)