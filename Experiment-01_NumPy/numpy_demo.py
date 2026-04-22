# Experiment 1: NumPy
# Aim: Perform basic numerical operations using NumPy

import numpy as np  # Import NumPy library

# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Display arrays
print("Array A:", a)
print("Array B:", b)

# Perform operations
print("Addition:", a + b)        # Element-wise addition
print("Mean of A:", np.mean(a))  # Calculate average