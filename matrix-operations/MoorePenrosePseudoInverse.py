# Ricardo Nader 10072023

# Standard matrix inverse operation not supports singular matrices.
# For these cases, aplying Moore Penrose PseudoInverse may be a solution

# Let's calculate the pseudoinverse  A+  of
# some matrix  A  using the formula from the slides:

# A+=VD+UT (U Transposed)

import numpy as np
