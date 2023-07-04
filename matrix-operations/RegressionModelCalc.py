#A regression model may have n number of equations. In this example we'll have 2.
# 4b + 2c = 4
#-5b - 3c = -7
#So from this elements we'll have one matrix with predictions, 
#one vector with outcomes so that we can solve for the unknowns(weights - w = Xy) 
#by obtaining the product from matrix inversion of our predictions times
#our vector. 

import numpy as np

print("- Defining predictions matrix")
X = np.array([[4,2],[-5,-3]])
print(X)
print("")

print("- Calculating matrix inversion")
Xinv = np.linalg.inv(X)
print(Xinv)
print("")

print("- Defining vector with outcomes")
y = np.array([4,-7])
print(y)
print("")

print("- Defining vector with outcomes")
w = np.dot(Xinv,y)
print(w)
print("")

#Confirming if the product from Xw will result in the vector y
print("- #Asserting that the result from y = Xw is correct")
print(np.dot(X,w))
print("")
