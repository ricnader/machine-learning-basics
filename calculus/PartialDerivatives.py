
# Partial Derivatives of Multivariate Functions

# Define a function  f(x,y) for z=x2−y2 :


import numpy as np
import matplotlib.pyplot as plt
import torch
import math # for constant pi

def f(my_x,my_y):
  return my_x**2 - my_y**2

xs = np.linspace(3,-3,3000)

zs_wrt_x = f(xs, 0)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')

plt.xlabel('x')
plt.ylabel('z', rotation=0)
_ = ax.plot(xs, zs_wrt_x)


def delz_delx(my_x,my_y):
  return 2*my_x

x_samples = [-2,-1,0,-1,-2]
colors = ['red', 'orange', 'green', 'blue', 'purple']

def point_and_tangent_wrt_x(my_xs, my_x, my_y, my_f, fprime, col):

    my_z = my_f(my_x, my_y) # z = f(x, y) 
    plt.scatter(my_x, my_z, c=col, zorder=3) 
    
    tangent_m = fprime(my_x, my_y) # Slope is partial derivative of f(x, y) w.r.t. x
    tangent_b = my_z - tangent_m*my_x # Line is z=mx+b, so b=z-mx
    tangent_line = tangent_m * my_xs + tangent_b

    # print(my_xs)
    # print(tangent_m * my_xs)    
    print("tangent_m: ",tangent_m)
    print("tangent_b: ",tangent_b)
    print("tangent_line: ",tangent_line)
    print("")
    plt.plot(my_xs, tangent_line, c=col, 
             linestyle='dashed', linewidth=0.7, zorder=3)


for i, x in enumerate(x_samples):
    point_and_tangent_wrt_x(xs, x, 0, f, delz_delx, colors[i])
