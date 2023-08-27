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

print("---> Generating Eigen Vectors/values")
PT = P.T
PPT_l, PPT_V = tr.linalg.eig(P * PT)
PTP_l, PTP_V = tr.linalg.eig(PT * P)

print("")
print("")

print("---> Asserting item 1")
print("Left-singular vectors of P:", U)
print("Eigen Vectors of PPT", PPT_V)
print(U == PPT_V)
print("")
print("---> Asserting item 2")
print("right-singular vectors of P:", VT)
print("Eigen Vectors of PTP", PTP_V)
print(VT == PTP_V)

print("")
print("")

print("---> Asserting item 3")
print("P == PPT == PPT:")
print(P == PPT_l)
print("")
print("P == PPT == PTP:")
print(P == PTP_l)

# Sqrt()
# print(y)
# print(V)
# print(V.t())
# print(P)
# print(PT)

# print("")
