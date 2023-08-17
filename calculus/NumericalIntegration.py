
# "quadrature" = numerical integration (as opposed to symbolic)
from scipy.integrate import quad 

# ∫2 1 x/2 dx= 34 
# (Definite integral # from 1 to 2 in the function of x/2)

#Defining the function
def g(x):
    return x/2
  
  
#Calling the scipy quad function to calculate
# and return the area under the curve between 1 and 2
print(quad(g, 1, 2))

#Result
# (0.75, 8.326672684688674e-15)
#This is the result expected from the function above.
#First parameter indicates that the distance between
# 1 and 2 in this curve corresponds to 3/4
# The second parameter corresponds to the estimate of error
# to do this integration. This estimate is necessary for numerical
# (computational) integration

# The second output of quad is an
# estimate of the absolute error of the integral,
# which in this case is essentially zero.