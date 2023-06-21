# By Ricardo Nader - 21062023

# It's analog to the L^2 norm for vectors.
# It's root of the sum of all squared numbers of an array

import torch
import numpy as np
import tensorflow as tf


print("- Defining array/matrix")
X = np.array([[1,2],[3,4]])
print(X)
print("")

print("- Manual Calculation")
print(f"(1**2 + 2**2 + 3**2 + 4**2) **(1/2): {(1**2 + 2**2 + 3**2 + 4**2) **(1/2)}")
print("")


print("- Using numPy")
print(np.linalg.norm(X))
print("")


print("- Using pyTorch")
# The tensor has to be of type float for this operation to work
# (thats the reason of putting a point after '4')
X_pt = torch.tensor([[1,2],[3,4.]])
print(torch.norm(X_pt))
print("")


print("- Using tensorFlow")
# The tensor has to be of type float for this operation to work
# (thats the reason of putting a point after '4')
X_tf = tf.Variable([[1,2],[3,4.]])
print(tf.norm(X_tf))
print("")