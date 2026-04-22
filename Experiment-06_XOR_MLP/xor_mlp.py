# Experiment 6: XOR using MLP
# Aim: Solve XOR problem using neural network

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])

# Build model
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))  # Hidden layer
model.add(Dense(1, activation='sigmoid'))            # Output layer

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy')

# Train model
model.fit(X, y, epochs=500, verbose=0)

# Predictions
print("Predicted Output:")
print(model.predict(X))