# Experiment 8: Multi-Layer Perceptron
# Aim: Build simple MLP model

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])

# Model
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile
model.compile(optimizer='adam', loss='binary_crossentropy')

# Train
model.fit(X, y, epochs=300, verbose=0)

print("Predictions:")
print(model.predict(X))