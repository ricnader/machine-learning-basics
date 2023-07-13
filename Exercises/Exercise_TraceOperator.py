# Exercises:

# With the matrix A_p provided below:
# tensor([[-1.,  2.],
#         [ 3., -2.],
#         [ 5.,  7.]])

# Use the PyTorch trace method to calculate the trace of A_p.
# Use the PyTorch Frobenius norm method and the trace method to
# demonstrate that  ||A||F=Tr(AAT)−−−−−−−−√

import torch as tr

print("- Defining matrix A_p")
A_p = tr.tensor([[-1, 2.], [3, -2.], [5, 7.]])
print(A_p)
print("")


print("Using trace")
print(tr.trace(A_p))
print("")

print("Using frobenius norm")


Z = tr.cat((A_p, tr.tensor([[0, 0, 0]]).T), 1)

print(Z.size)
# z = (Z * A_p.T)
# print(tr.norm(z, p='fro'))
# print("")
