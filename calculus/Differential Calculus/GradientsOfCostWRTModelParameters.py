# Let's use the same data as we did in the Regression 
# in PyTorch 

# !keep in mind!
# The slope of a line is given by  y= mx+b

#-----------------------------------------------------------------------
# Step 1: Forward pass

# We can flow the scalar tensor x  
# through our regression model to produce
# y^ ,an estimate of y.

# Prior to any model training, this is an arbitrary estimate:

#-----------------------------------------------------------------------
# Step 2: Compare y^ with true y to calculate cost C

# We previously used mean-squared error, which averages quadratic 
# cost over multiple data points. 
# With a single data point, here we can use quadratic cost alone. 
# It is defined by:C=(y^−y)2


#-----------------------------------------------------------------------
# Step 3: Use autodiff to calculate gradient of C w.r.t. parameters
# --  Define the partial derivative of  C with respect to b  ( ∂C/∂m )
# --  Define the partial derivative of  C with respect to b  ( ∂C/∂b )

#-----------------------------------------------------------------------

import numpy as np
import torch as tr



import torch


print("Defining xs")
xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.]) # E.g.: Dosage of drug for treating Alzheimer's disease
print(xs)
print("")



print("Defining ys sample vector")
ys = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37]) # E.g.: Patient's "forgetfulness score"
print(ys)
print("")

print("Defining method for calculating the slope")
def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b
  
m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()

print("Taking 'random' values from the samples "
      "for testing with index = 7")
i = 7
x = xs[i]
y = ys[i]
print("x: ",x)
print("y: ",y)
print("")

#-----------------------------------------------------------------------
# Step 1: Forward pass

print("Resulting yhat is:")
yhat = regression(x, m, b)
print(yhat)
print("")

#-----------------------------------------------------------------------
# Step 2: Compare y^ with true y to calculate cost C

def squared_error(my_yhat, my_y):
    return (my_yhat - my_y)**2

print("C (cost) for the given inputs in relation to yhat")  
C = squared_error(yhat, y)
print(C)
print("")

#-----------------------------------------------------------------------
# Step 3: Use autodiff to calculate gradient of C w.r.t. parameters
C.backward()

# --  Define the partial derivative of  C with respect to b  ( ∂C/∂m )
print("Gradient of m: ",m.grad)
print(m.grad)
print("")
# --  Define the partial derivative of  C with respect to b  ( ∂C/∂b )
print("Gradient of b: ",b.grad)
print(b.grad)
print("")

#After manually calculating the gradient descent of cost we
#arrive to the following formula ∂C/∂m= 2x(y^−y) and ∂C/∂b=2(y^−y)

#This is means is that if we want to do the autodiff manually
#we must apply this formla to the given context and we should get
#the same results

print("∂C/∂m= 2x(y^−y): ",2*x*(yhat.item()-y))

print("∂C/∂b=2(y^−y): ",2*(yhat.item()-y))