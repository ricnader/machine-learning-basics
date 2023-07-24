# The derivative of y (denoted dy) with respect to x (denoted dx ) can be represented as:
# dy/dx = limΔx→0 Δy/Δx


# Expanding Δy out to y2−y1:
#  dy/dx = lim Δx→0 y2−y1/Δx

# Finally,replacing y1 with f(x)  
# and replacing y2 with f(x + Δx), 
# we obtain a common representation of differentiation:
# dy/dx = lim Δx→0  f(x + Δx)-f(x)/Δx 

import numpy as np
import matplotlib.pyplot as plt

print("Defining x as start, finish and n points")
x = np.linspace(-10, 10, 10000) 
print("")

print("Defining y")
y = x**2 + 2*x + 2
print("")

print("For some kind of simple functions we can take a result empirically \n"+
      "So, trying to get close infinitelly of the unknow")
def my_fxn(my_x):
    my_y = (my_x**2 - 1)/(my_x - 1)
    return my_y

y = my_fxn(x)

# plt.show();