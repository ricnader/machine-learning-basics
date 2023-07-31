# A.K.A:
# AutoDiff
# AutoGrad
# Computational diff
# Reverse mode diff
# Algorithmic diff

# Distinct from classical methods
#   - Numerical diff.(delta method; Introduces rounding errors)
#   - Symbolic diff. (algebraic rules; computationally inefficient)

# Relative to classical methods, better handles:
#   - Functions with many inputs (common in ML)
#   - Higher-order derivatives

# TensorFlow and PyTorch are the two most popular automatic differentiation libraries.

# Let's use them to calculate dy/dx at x = 5 where:

# y = x2

# dy/dx = 2x = 2(5) = 10


import torch
import tensorflow as tf

#with pyTorch
print("Using pyTorch")    
print("Defining x")
x = torch.tensor(5.0)
print(x)
print("")


# contagiously track gradients through forward pass
x.requires_grad_() 

print("Defining y")
y = x**2
print(y)
print("")

print("Using Autodiff")
y.backward() # use autodiff
print(x.grad)
print("")


#with tensorFlow
x = tf.Variable(5.0)

with tf.GradientTape() as t:
    t.watch(x) # track forward pass
    y = x**2
    
print("Using tensorFlow")    
print(t.gradient(y, x)) # use autodiff 

print("")