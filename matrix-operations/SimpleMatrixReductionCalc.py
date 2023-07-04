# Calculating the sum across all elements of a tensor is a common operation. For example:

# For vector x of length n, we calculate  ∑ni=1xi 
# For matrix X with m by n dimensions, we calculate  ∑mi=1 ∑nj=1Xi,j 




import torch
import numpy as np
import tensorflow as tf

print("- Defining array/matrix")
# type argument is optional, e.g.: dtype=np.float16
X= np.array([[25,2,5],[41,85,2],[8,0,33]])
print(X)
print("")

print("- Simple way of reducting the matrix")
print("X.sum() = ",X.sum())
print("")


print("- Using pyTorch for reducting the matrix")
X_pt = torch.tensor([[25,2,5],[41,85,2],[8,0,33]])
print("torch.sum() = ", torch.sum(X_pt))
print("")

print("- Using TensorFlor for reducting the matrix")
X_tf = torch.tensor([[25,2,5],[41,85,2],[8,0,33]])
print("tf.reduce_sum(X_tf) = ", tf.reduce_sum(X_tf))
print("")