# Experiment 3: SciPy
# Aim: Perform scientific computations using SciPy

from scipy import integrate, optimize

# ---------------------------
# Integration Example
# ---------------------------
# Define function f(x) = x^2
def func(x):
    return x**2

# Integrate from 0 to 2
result, error = integrate.quad(func, 0, 2)

print("Integration Result:", result)
print("Estimated Error:", error)

# ---------------------------
# Optimization Example
# ---------------------------
# Define function f(x) = x^2 + 3x + 2
def func2(x):
    return x**2 + 3*x + 2

# Find minimum
res = optimize.minimize(func2, x0=0)

print("Minimum Value:", res.fun)
print("Value of x at minimum:", res.x)