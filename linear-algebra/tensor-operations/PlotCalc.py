# Not graphically Functional yet

import numpy as np
import matplotlib.pyplot as plt


print("- Defining x")
x = np.linspace(-10, 10, 1000)
print("")


print("- Defining y1")
y1 = 3 * x
print("")


print("- Defining y2")
y2 = 1 + (5*x) / 2
print("")

print("- Setting up the plot")
fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim([0, 3])
ax.set_ylim([0, 8])
ax.plot(x, y1, c="green")
ax.plot(x, y2, c="brown")
plt.axvline(x=2, color="purple", linestyle='--')
_ = plt.axhline(y=6, color="purple", linestyle='--')

plt.show()
