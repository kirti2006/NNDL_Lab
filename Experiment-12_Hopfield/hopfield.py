# Experiment 12: Hopfield Network
# Aim: Implement associative memory

import numpy as np

# Pattern
p = np.array([1,-1,1,-1])

# Weight matrix
W = np.outer(p,p)
np.fill_diagonal(W,0)

# Test input
x = np.array([1,-1,1,-1])

# Update
for i in range(5):
    x = np.sign(np.dot(W,x))

print("Recovered Pattern:", x)