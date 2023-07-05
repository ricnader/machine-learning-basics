# by Ricardo Nader  - 07052023

# SVD and eigendecomposition are closely related to each other:

# 1- Left-singular vectors of  A  = eigenvectors of  AAT(A*A Transposed).
# 2- Right-singular vectors of  A  = eigenvectors of  ATA(A*A Transposed).
# 3- Non-zero singular values of  A  = square roots of eigenvalues
#   of  AAT  = square roots of eigenvalues of  ATA

# EXERCISE: Using the matrix P from the preceding PyTorch exercises,
#   demonstrate that these three SVD-eigendecomposition equations are true.

import torch as tr

print("- Defining matrix P")
P = tr.tensor([[25, 2, -5], [3, -2, 1], [5, 7, 4.]])
print(P)
print("")

print("****> Asserting item 1")
print("Defining SVD from P")
U, d, VT = tr.linalg.svd(P)
print("")

print("---> Asserting item 1")
# print(U == (V*V.t()))
lambdas, V = tr.linalg.eig(P)
PT = P.T
y = V * PT
z = V * P


print(U)
print(y)
print(U == y)

# print(y)
# print(V)
# print(V.t())
# print(P)
# print(PT)

# print("")
