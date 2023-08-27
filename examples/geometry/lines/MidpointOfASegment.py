import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()
# x = np.linspace(-np.pi, np.pi, 100)
# y = 2 * np.sin(x)

# ax = fig.add_subplot(5, 5, 1)
# ax.set_title('centered spines')
# ax.plot(x, y)
# plt.show()
x = np.array([1,5])
y = np.array([2,7])

fig = plt.figure()
ax = fig.add_subplot(5, 5, 1)
ax.set_title('centered spines')
ax.plot(x, y)
plt.show()

# # plt.plot_vectors([[-3,3],[1,3]],["green","blue"])
# x = np.array([[-1,1],[2,3]],[[2,2],[5,4]])
# plt.plot(x)
# plt.show()
# plt.ylim(min(y), max(y))
# plt.xlim(min(x), max(x))
# plt.plot(x,y)
# plt.show()