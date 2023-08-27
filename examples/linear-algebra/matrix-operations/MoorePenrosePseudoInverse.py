# Ricardo Nader 10072023

# Standard matrix inverse operation not supports singular matrices.
# For these cases, aplying Moore Penrose PseudoInverse may be a solution

# Let's calculate the pseudoinverse  A+  of
# some matrix  A  using the formula from the slides:

# We're talking about assymetric matrices so for decomposition we must
# use Singule Value Decomposition(SVD)

# A+ = VD+(PseudoInverse of D) UT (U Transposed)

import numpy as np


print("-Defining Matrix A")
A = np.array([[-1, 2], [3, -2], [5, 7]])
print("")

print("-Decomposing A")
U, d, VT = np.linalg.svd(A)
print("")


print("-Left vectors of A")
print(U)
print("")

print("-Diag of singular values")
print(d)
print("")

print("-Right vectors(transposed) of A")
print(VT)
print("")


print("To create  D+ , we first invert the non-zero values of  d :")
D = np.diag(d)
Dinv = np.linalg.inv(D)
print("D+ = ")
print(Dinv)
print("")

print("D+  must have the same dimensions as  AT  in order for \n" +
      "VD+UT  matrix multiplication to be possible: ")
Dplus = np.concatenate((Dinv, np.array([[0, 0]]).T), axis=1)
print(Dplus)
print("")

print("(Recall  D  must have the same dimensions as  A  for SVD's \n" +
      "UDVT , but for MPP  U  and  V  have swapped sides around the diagonal matrix.)")

print("")
print("")

print("Now we have everything we need to calculate  A+  with  VD+UT :")
# VT is transposed here to become a "normal" V, since it comes
# transposed from svd decomposition
print(np.dot(VT.T, np.dot(Dplus, U.T)))
print("")
print("-----------------------------------------------------------------")
print("")
print("Alternatively we can simply use the built in method for numPy: ")
print(np.linalg.pinv(A))
print("")
