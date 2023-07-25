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

# print("Defining y")
# y = x**2 + 2*x + 2
# print("")

print("Creating function for finding the y\n"
      "given an x and an y-intercept")
def f(my_x):
    my_y = my_x**2 + 2*my_x + 2
    return my_y
print("")

print("Defining y")
y = f(x)
print(y)
print("")

#According to the explanation on top of this file
#lets create our function to calculate the derivarives
print("Creating function that calcs the derivatives")

def diff_demo(my_f, my_x, my_delta):
    return (my_f(my_x + my_delta) - my_f(my_x)) / my_delta
print("")

print("Creating array to simulate some deltas")

deltas = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
print("")


print("Iterating through deltas, calculating derivatives")
print("Pay attention to how close the value becames to y")
print("through each calculation")
print("x equals to 2")

for delta in deltas:
    print(diff_demo(f, 2, delta))
    print("")
    
print("x equals to -1")    

for delta in deltas:
    print(diff_demo(f, -1, delta))
print("")
# plt.show();