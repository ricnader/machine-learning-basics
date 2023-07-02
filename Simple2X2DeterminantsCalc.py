# det(X) = product of all eigenvalues of X

# (For 2x2 matrices)
# if
# |a b|
# |c d|
# then
# |X| = ad-bc

# |det(X)| quantifies volume change as a result of applying X:
# - If det(X) = 0, then X collapses space completely in at least
#   one dimension, thereby elimination all volume. In this case
#   we'll be dealing with a singular matrix (with paralel or infinite results)
#
# - If 0 < |det(X)| < 1 then X contracts volume to some extent  
# - If |det(X)| = 1 then X preserves volume exactly
# - If |det(X)| > 1 then X expands volume

import numpy as np

print("- Defining Matrix")
X = np.array([[4,2],[-5,-3]])
print(X)
print("")

print("- Calculating the determinant of X")
det = np.linalg.det(X)
print(det)



