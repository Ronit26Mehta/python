from scipy.integrate import quad
from scipy.special import beta

# Define the parameters
a = 5
b = 2

# Define the integrand function
def integrand(x):
    return (1 / beta(a, b)) * x**(a - 1) * (1 - x)**(b - 1)

# Integrate the function over the range [0.2, 0.3]
result, _ = quad(integrand, 0.2, 0.3)

print(result)
