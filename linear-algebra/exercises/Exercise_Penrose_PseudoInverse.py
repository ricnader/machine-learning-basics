# Ricardo Nader 07112023

# Standard matrix inverse operation not supports singular matrices.
# For these cases, aplying Moore Penrose PseudoInverse may be a solution

# Let's calculate the pseudoinverse  A+  of
# some matrix  A  using the formula from the slides:

# We're talking about assymetric matrices so for decomposition we must
# use Singule Value Decomposition(SVD)

# A+ = VD+(PseudoInverse of D) UT (U Transposed)

# Use the torch.svd()
# method to calculate the pseudoinverse of A_p,
# confirming that your result matches the output of torch.pinverse(A_p):

import torch as tr


print("- Defining matrix A_p")
A_p = tr.tensor([[-1, 2], [3, 2], [5, 7.]])
print(A_p)

print("Decomposing A")
U, d, VT = tr.linalg.svd(A_p)
print("")

print("U")
print(U)
print("")

print("d")
print(d)
print("")

print("VT")
print(VT)
print("")

print("Creating Diag of d")
D = tr.diag(d)
print(D)
print("")

print("Inverting d")
Dinv = tr.linalg.inv(D)
print(Dinv)
print("")

print("Concatenating new column for final multiplication")
Dplus = tr.cat((Dinv, tr.tensor([[0, 0]]).T), 1)
print(Dplus)
print("")

print("Manual Result:")
result = tr.matmul(VT.T, (tr.matmul(Dplus, U.T)))
print(result)
print("")

print("Result with built in method:")
print(tr.pinverse(A_p))
