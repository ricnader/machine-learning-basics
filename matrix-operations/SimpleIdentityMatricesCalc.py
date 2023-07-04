# identity matrices are composed only by 1s and 0s. 
# In an operation with any other type of vector/matrix 
# the result will be equals to the non identity vector/matrix

import torch

print("- Defining identity matrix")
X_idt = torch.tensor([[1,0,0],[0,1,0],[0,0,1]])
print(X_idt)
print("")

print("- Defining standard vector")
y = torch.tensor([25,85,42])
print(y)
print("")

print("- Multiplying the two (Result is equal to vector y)")
print(torch.matmul(X_idt,y))
print("")


