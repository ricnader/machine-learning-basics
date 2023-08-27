# The volume of a cylinder is described 
# by v= πr**2l where:

# r  is the radius of the cylinder
# l  is its length


import numpy as np
import torch as tr
import math # for constant pi


print("Defining a formula for a cylinder")
def cylinder_vol(my_r,my_l):
  return math.pi * my_r**2 * my_l

print("Radius of 3 meters")
r = tr.tensor(3.).requires_grad_()
print(r)
print("")

print("A Length of 5 meters")
l = tr.tensor(5.).requires_grad_()
print(l)
print("")
  
#Calculating the overall volume  
v = cylinder_vol(r,l)

#Applying autodiff (auto differentiation)
v.backward()


print("The change in v for each unit of l if r is 3 is:")
print(l.grad)
print("")

