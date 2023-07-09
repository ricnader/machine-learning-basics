#Ricardo Nader 20230907

# det(X) = product of all eigenvalues of X

# (For 2x2 matrices)
# if
# |a b|
# |c d|
# then
# |X| = ad-bc


import numpy as np

print("- Defining matrix X")
X = np.array([[4,2],[-5,-3]])
print(X)
print("")

print("- Calculating the determinant of X")
detX = np.linalg.det(X)
print(detX)
print("")



