# Experiment 7: Activation Functions
# Aim: Implement Sigmoid and ReLU

import numpy as np

# Input values
x = np.array([-2, -1, 0, 1, 2])

# Sigmoid function
sigmoid = 1 / (1 + np.exp(-x))

# ReLU function
relu = np.maximum(0, x)

print("Input:", x)
print("Sigmoid:", sigmoid)
print("ReLU:", relu)