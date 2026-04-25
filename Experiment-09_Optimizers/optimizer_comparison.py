# Experiment 9: Optimizers (Gradient Descent + Adam)

import numpy as np

# Function: f(x) = x^2
def f(x):
    return x**2

def grad(x):
    return 2*x


# ==============================
# Gradient Descent
# ==============================
print("\n--- Gradient Descent ---")

x = 5
lr = 0.1

for i in range(10):
    g = grad(x)
    x = x - lr * g
    print(f"Step {i+1}: x = {x}")

print("Final GD Value:", x)


# ==============================
# Adam Optimizer
# ==============================
print("\n--- Adam Optimizer ---")

x = 5
lr = 0.1

beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8

m = 0
v = 0

for t in range(1, 11):
    g = grad(x)

    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * (g**2)

    m_hat = m / (1 - beta1**t)
    v_hat = v / (1 - beta2**t)

    x = x - lr * m_hat / (np.sqrt(v_hat) + epsilon)

    print(f"Step {t}: x = {x}")

print("Final Adam Value:", x)