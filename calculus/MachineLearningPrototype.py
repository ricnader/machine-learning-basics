
import torch
import tensorflow as tf

# #with pyTorch
# print("Using pyTorch")    
# print("Defining x")
# x = torch.tensor(5.0)
# print(x)
# print("")


# # contagiously track gradients through forward pass
# x.requires_grad_() 

# print("Defining y")
# y = x**2
# print(y)
# print("")

# print("Using Autodiff")
# y.backward() # use autodiff
# print(x.grad)
# print("")


# #with tensorFlow
# x = tf.Variable(5.0)

# with tf.GradientTape() as t:
#     t.watch(x) # track forward pass
#     y = x**2
    
# print("Using tensorFlow")    
# print(t.gradient(y, x)) # use autodiff 

# print("")