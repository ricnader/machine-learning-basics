# The Calculus of Infinitesimals

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



fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axvline(x=1, color='purple', linestyle='--')
plt.axhline(y=2, color='purple', linestyle='--')
_ = ax.plot(x,y)




print("For more complex functions like one usin a SIN fuction \n"+
      "we can use another method")

def sin_fxn(my_x):
    my_y = np.sin(my_x)/my_x
    return my_y
  
y = sin_fxn(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-10, 10)
plt.ylim(-1, 2)
plt.axvline(x=0, color='purple', linestyle='--')
plt.axhline(y=1, color='purple', linestyle='--')
_ = ax.plot(x,y)

plt.show();