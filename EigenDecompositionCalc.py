# The eigendecomposition of some matrix  A  is
# A=VΛV−1  (Λ being uppercase lambda)

# Where:

# - As in examples above,  V  is the concatenation of all
# the eigenvectors of  A
# - Λ  (upper-case  λ ) is the diagonal matrix diag( λ ).
# Note that the convention is to arrange the lambda values
# in descending order; as a result, the first eigenvalue
# (and its associated eigenvector) may be a primary
# characteristic of the matrix  A .

import numpy as np

print("- Defining matrix A")
A = np.array([[4, 2], [-5, -3]])
print(A)
print("")

print("- Calculating EigenVectors from A")
lambdas, V = np.linalg.eig(A)
print(V)

print("- Inverting EigenVector")
Vinv = np.linalg.inv(V)
print(Vinv)
print("")

print("- Creating diagonal matrix (Λ) from eigenValues")
Lambda = np.diag(lambdas)
print(Lambda)
print("")

print("- Confirm that A=VΛV−1 (It has to be equal to initial Matrix A):")
print(np.dot(V, np.dot(Lambda, Vinv)))
print("")
