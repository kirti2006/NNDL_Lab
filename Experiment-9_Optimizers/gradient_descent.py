# Experiment 9: Optimizer (Gradient Descent)
# Aim: Demonstrate gradient descent

# Initial value
x = 5
lr = 0.1

# Iteration
for i in range(10):
    grad = 2 * x      # derivative of x^2
    x = x - lr * grad

print("Optimized Value:", x)