
# Evaluate the following expression:
#∫43 2xdx 

# "quadrature" = numerical integration (as opposed to symbolic)
from scipy.integrate import quad 


#Defining the function
def g(x):
    return 2*x
  
  
#Calling the scipy quad function to calculate
# and return the area under the curve between 3 and 4
print(quad(g, 4,3))
