# Ricardo Nader 07132023

# The trace operator has a number of useful properties that come in handy while rearranging linear algebra equations, e.g.:

# Tr(A) = Tr(AT)
# Assuming the matrix shapes line up: Tr(ABC) = Tr(CAB) = Tr(BCA)
# In particular, the trace operator can provide a convenient way to calculate a matrix's Frobenius norm:
# ||A||F=Tr(AAT)−−−−−−−−√

import torch
import numpy as np
import tensorflow as tf


print("- Defining array/matrix")
A = np.array([[25, 2], [5, 4]])
print(A)
print("")

print("Manual calc")
print(25+4)
print("")

print("Using trace")
print(np.trace(A))
print("")
