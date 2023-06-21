# By Ricardo Nader - 21062023

import torch
import numpy as np
import tensorflow as tf


print("- Defining matrix")
A = np.array([[1,2],[3,4],[5,6]])
print(A)
print("")

print("- Defining vector")
b = np.array([7,8])
print(b)
print("")

print("- Calculating with nymPy")
print(np.dot(A,b))
print("")


print("- Defining matrix for pyTorch")
A_pt = torch.tensor([[1,2],[3,4],[5,6]])
print(A_pt)
print("")

print("- Defining vector for pyTorch")
b_pt = torch.tensor([7,8])
print(b_pt)
print("")

print("- Calculating with pyTorch")
print(torch.matmul(A_pt,b_pt))
print("")


print("- Defining matrix for tensorFlow")
A_tf = tf.Variable([[1,2],[3,4],[5,6]])
print(A_tf)
print("")

print("- Defining vector for tensorFlow")
b_tf = tf.Variable([7,8])
print(b_tf)
print("")

print("- Calculating with tensorFlow")
print(tf.linalg.matvec(A_pt,b_pt))
print("")
