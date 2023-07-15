# Exercises:

#  1 - Use PyTorch to decompose the matrix  P  (below)
#     into its components  V ,  Λ , and  V−1 . Confirm that  P=VΛV−1 .
#  2 - Use PyTorch to decompose the symmetric matrix  S
#     (below) into its components  Q ,  Λ , and  QT . Confirm that  S=QΛQT .

import torch as tr

print("- Defining matrix P")
P = tr.tensor([[4, 2], [-5, -3.]])
print(P)
print("")

print("- Calculating EigenVectors from P")
lambdas, V = tr.linalg.eig(P)
print(V)
print("")

print("- Inverting EigenVector")
Vinv = tr.linalg.inv(V)
print(Vinv)
print("")

print("- Current lambdas")
print(lambdas)
print("")

print("- Creating diagonal matrix (Λ) from eigenValues")
Lambda = tr.diag(lambdas)
print(Lambda)
print("")

print("- Confirm that P=VΛV−1 (It has to be equal to initial Matrix A):")
print(tr.matmul(V, tr.matmul(Lambda, Vinv)))
print("")
