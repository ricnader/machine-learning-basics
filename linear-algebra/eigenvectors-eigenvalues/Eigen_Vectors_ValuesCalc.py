#Ricardo Nader 20230907

# An eigenvector (eigen is German for "typical"; 
# we could translate eigenvector to "characteristic vector") 
# is a special vector  v  such that when it is transformed by some matrix 
# (let's say  A ), the product  Av  has the exact same direction as  v .

# An eigenvalue is a scalar (traditionally represented as  λ ) 
# that simply scales the eigenvector  v  such that the following equation is satisfied:

# Av=λv

import torch
import numpy as np

print("- Defining Matrix")
# type argument is optional, e.g.: dtype=np.float16
X = np.array([[-1,4],[2,-2]])
print(X)
print("")

print("- Return eigen vectors/values in a tuple based o matrix X:")
print("lambdas, V = np.linalg.eig(X)") 
lambdas, V = np.linalg.eig(X) 
print("")

print("- The matrix contains as many eigenvectors as there are columns of A:")
print(V)
print("")

print("- With a corresponding eigenvalue for each eigenvector:")
print(lambdas)
print("")

print("- Let's confirm that  Av=λv  for the first eigenvector:")
v = V[:,0] 
lambd = lambdas[0]
print(v) 
print("")

print("- The results match")
Av = np.dot(X, v)
print("Av = np.dot(A, v):")
print(Av) 
print("")
print("lambd * v:")
print(lambd * v)
print("")



print("And again for the second eigenvector of A:")
v2 = V[:,1]
print(v2)
lmbd2 = lambdas[1]
print(lmbd2)

print("- The results also match")
print("Av2 = np.dot(A, v2):")
Av2 = np.dot(X, v2)
print(Av2)
print("")
print("lmbd2 * v2:")
print(lmbd2 * v2)
print("")
