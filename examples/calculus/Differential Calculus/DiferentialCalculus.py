# Diferential Calculus previously known 
# as The Calculus of Infinitesimals

import numpy as np
import matplotlib.pyplot as plt

print("Defining x as start, finish and n points")
x = np.linspace(-10, 10, 10000) 
print("")

print("Defining y")
y = x**2 + 2*x + 2
print("")

print("Showing graphs")
fig, ax = plt.subplots()
_ = ax.plot(x,y)
plt.show();
print("")

print("Zooming in to try to find the tangent of the curve")
print("")
fig, ax = plt.subplots()
ax.set_xlim([-2, -0])
ax.set_ylim([0, 2])
_ = ax.plot(x,y)

fig, ax = plt.subplots()
ax.set_xlim([-1.5, -0.5])
ax.set_ylim([0.5, 1.5])
_ = ax.plot(x,y)

fig, ax = plt.subplots()
ax.set_xlim([-1.1, -0.9])
ax.set_ylim([0.9, 1.1])
_ = ax.plot(x,y)

fig, ax = plt.subplots()
ax.set_xlim([-1.01, -0.99])
ax.set_ylim([0.99, 1.01])
_ = ax.plot(x,y)
plt.show();