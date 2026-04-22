# Experiment 5: Perceptron
# Aim: Implement perceptron for AND gate

import numpy as np

# Input dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# Initialize weights
w = np.zeros(2)
lr = 0.1

# Training process
for epoch in range(10):
    for i in range(len(X)):
        output = np.dot(X[i], w)
        pred = 1 if output > 0 else 0
        w += lr * (y[i] - pred) * X[i]

# Output weights
print("Final Weights:", w)