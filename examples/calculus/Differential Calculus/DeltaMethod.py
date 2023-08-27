# To find the slope m between points P and Q:
# m = change in y / ychange in x
# x = Δy/Δx 
# = y2-y1 / x2-x1 
# = 37-10 / 5-2 = 273 = 9

#for the equation for calculating the y value based on x and y-intercept
#y = mx+b where b is the y-intercept


import numpy as np
import matplotlib.pyplot as plt

print("Defining x as start, finish and n points")
x = np.linspace(-10, 10, 10000) 
print(x)
print("")

#Using the same expression from other calculus examples
def f(my_x):
    my_y = my_x**2 + 2*my_x + 2
    return my_y

print("Defining y")
y = f(x)
print(y)
print("")


print("plotting curve")

fig, ax = plt.subplots()
ax.set_title('Basic curve')
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
_ = ax.plot(x,y)

print("")

print("for test purposes, lets identify the slope of 2 for example")
print(f(2))
print("")

print("Cool. Let's call this point P, which is located at (2, 10):")
fig, ax = plt.subplots()
ax.set_title('Including point P')
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10) # new
_ = ax.plot(x,y)


print("")

print("# The delta method uses the difference between two points to calculate slope.\n"+ 
"To illustrate this, let's define another point, Q where, say, x=5")
print(f(5))
print("")

fig, ax = plt.subplots()
ax.set_title('Including point Q')
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)
plt.scatter(5, 37, c = 'orange', zorder=3) # new
_ = ax.plot(x,y)


print("Using the delta method for finding the slope of the points")
m = (37-10)/(5-2)
print("m = (37-10)/(5-2) = ",m)
print("")

print("To plot the line that passes through  P  and  Q , \n"
"we can rearrange the equation of a line y = mx+b to solve for b: b = y-mx")
b = 37-m*5
print(b)
print("")
line_y = m*x + b
print("line_y = m*x + b = ",line_y)
print("")


fig, ax = plt.subplots()
ax.set_title('Slope of the two points')
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)
plt.scatter(5, 37, c='orange', zorder=3)
plt.ylim(-5, 150) # new
plt.plot(x, line_y, c='orange') # new
_ = ax.plot(x,y)


print("The closer Q becomes to P, the closer the slope m \n"
"comes to being the true tangent of the point P.\n"  
"Let's demonstrate this with another point Q at x = 2.1.")
print("")
print("")

print("Previously, our Δx between Q and P was equal to 3. Now it is much smaller:")
print("Δx = x2-x1 = 2.1-2 = 0.1")
print(f(2.1))
print("")

fig, ax = plt.subplots()
ax.set_title('Distance of the two points getting smaller')
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)
plt.scatter(2.1, 10.61, c = 'orange', zorder=3)
_ = ax.plot(x,y)

print("New value for the slope")
m = (10.61-10)/(2.1-2)
print("m = (10.61-10)/(2.1-2) = ",m)
print("")

print("New value of b")
b = 10.61 - m * 2.1
print("b = 10.61 - m * 2.1 = ",b)
print("")
# plt.show()
print("So the close Q becomes to P (i.e., Δx approaches 0)\n"
      "the clearer it becomes that the slope m at point  P =\n "
      "(2, 10) is equal to 6.")

print("")
print("")

print("Let's make Δx extremely small, 0.000001, to illustrate this:")
delta_x = 0.000001
print("delta_x = 0.000001 or ", delta_x)
print("")

x1 = 2
y1 = 10


print("Rearranging  Δx=x2−x1 , we can calculate  x2\n"  
      "for our point Q, which is now extremely close to  P: x2 = x1 + Δx")
x2 = x1 + delta_x
print("x2 = ",x2)
print("")

y2 = f(x2)
print("y2 = ",y2)
print("")

print("To find the slope m, we continue to use:")
m = (y2 - y1)/(x2 - x1)
print("m = (y2 - y1)/(x2 - x1). m = ",m)

print("and with this value we could assume that we have a tangent for the point")