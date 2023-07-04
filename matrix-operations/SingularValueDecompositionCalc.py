# As on slides, SVD of matrix  A  is:

# A=UDVT

# Where:

# U  is an orthogonal  m×m  matrix; its columns are the left-singular vectors of  A .
# V  is an orthogonal  n×n  matrix; its columns are the right-singular vectors of  A .
# D  is a diagonal  m×n  matrix; elements along its diagonal are the singular values of  A .

import numpy as np

print("- Defining matrix A")
A = np.array([[-1, 2], [3, -2], [5, 7]])
print(A)
print("")

print("- Singular value decomposing A")
U, d, VT = np.linalg.svd(A)
print("U:")
print(U)
print("")
print("d:")
print(d)
print("")
print("VT:")
print(VT)
print("")
