# det(X) = product of all eigenvalues of X

# |det(X)| quantifies volume change as a result of applying X:
# - If det(X) = 0, then X collapses space completely in at least
#   one dimension, thereby elimination all volume. In this case
#   we'll be dealing with a singular matrix (with paralel or infinite results)
#
# - If 0 < |det(X)| < 1 then X contracts volume to some extent  
# - If |det(X)| = 1 then X preserves volume exactly
# - If |det(X)| > 1 then X expands volume

import numpy as np

print("- Defining matrix X")
X = np.array([[4,2],[-5,-3]])
print(X)
print("")

print("- Calculating the determinant of X")
detX = np.linalg.det(X)
print(detX)
print("")

print("- Defining a basis vector composed matrix B")
B = np.array([[1,0],[0,1]])
print(B)
print("")

print("- Defining a singular matrix N")
N = np.array([[-4,1],[-8,2]])
print(N)
print("")

print("- Calculating the determinant of N")
detN = np.linalg.det(N)
print(detN)
print("")

print("- Applying N to B")
NB = np.dot(N,B)
print(NB)
print("")

print("- Calculating EigenValues from N")
lambdas,V = np.linalg.eig(N)
print(lambdas)
# If any one of a matrix's eigenvalues is zero, 
# then the product of the eigenvalues must be zero and the 
# determinant must also be zero.
print(V)
print("")