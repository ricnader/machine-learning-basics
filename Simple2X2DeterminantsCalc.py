# det(X) = product of all eigenvalues of X

# |det(X)| quantifies volume change as a result of applying X:
# - If det(X) = 0, then X collapses space completely in at least
#   one dimension, thereby elimination all volume. In this case
#   we'll be dealing with a singular matrix (with paralel or infinite results)
#
# - If 0 < |det(X)| < 1 then X contracts volume to some extent  
# - If |det(X)| = 1 then X preserves volume exactly
# - If |det(X)| > 1 then X expands volume

import torch
import numpy as np

print("- Defining Matrix")
# type argument is optional, e.g.: dtype=np.float16
X = np.array([[-1,4],[2,-2]])
print(X)
print("")
