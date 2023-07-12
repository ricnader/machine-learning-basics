# Ricardo Nader 10072023

# w= x+(Pseudoinverted)y


# In this example X is a non square matrix of features is used as
# an input of # drug dosages being used together with the level
# of memory recovery  for alzheimer patients.

# x1 = [0, 1, 2, 3, 4, 5, 6, 7.] E.g.: Dosage of drug for treating Alzheimer's disease
# y = [1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37]  E.g.: Patient's memory recovery

# Goal is to get a prediction of sucess given a determined dosage.


import numpy as np
import matplotlib.pyplot as plt


print("-Defining Matrix x1")
x1 = np.array([[0, 1, 2, 3, 4, 5, 6, 7.]])
print(x1)
print("")

print("-Defining Matrix y")
y = np.array([[1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37]])
print(y)
print("")

print("Setting plot before solving for the unknowns \n" +
      "(close plot window to continue)")
title = 'Clinical Trial (before solving)'
xlabel = 'Drug dosage (mL)'
ylabel = 'Forgetfulness'
fig, ax = plt.subplots()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
_ = ax.scatter(x1, y)
# plt.show()
print("")

# Although it appears there is only one predictor ( x1 ),
# our model requires a second one (let's call it  x0 )
# in order to allow for a  y -intercept. Without this second
# variable, the line we fit to the plot would need to pass through the origin (0, 0). The  y -intercept is constant across all the points so we can set it equal to 1 across the board:

print("Creating constant y=1 intercept")
x0 = np.ones(8)
print(x0)
print("")

print("Concatenating x0 and x1")
X = np.concatenate((np.matrix(x0).T, np.matrix(x1).T), axis=1)
print(X)
print("")

print("Solving for w")
w = np.dot(np.linalg.pinv(X), y.T)
print(w)
print("")

print("Isolating values from w")
print("")
print("The first weight corresponds to the  y -intercept of \n" +
      "the line, which is typically denoted as  b :")
b = np.asarray(w).reshape(-1)[0]
print(b)
print("")
print("")

print("While the second weight corresponds to the slope of \n" +
      "the line, which is typically denoted as  m :")
m = np.asarray(w).reshape(-1)[1]
print(m)


print("Setting final plot(solved)")
fig, ax = plt.subplots()
new_title = 'Clinical Trial (after solving)'
plt.title(new_title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

ax.scatter(x1, y)

x_min, x_max = ax.get_xlim()
y_at_xmin = m*x_min + b
y_at_xmax = m*x_max + b

ax.set_xlim([x_min, x_max])
_ = ax.plot([x_min, x_max], [y_at_xmin, y_at_xmax], c='C01')

plt.show()
