# Experiment 11: RNN
# Aim: Implement simple RNN

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Dummy sequence data
X = np.random.rand(10,5,1)
y = np.random.randint(0,2,10)

# Model
model = Sequential()
model.add(SimpleRNN(10, input_shape=(5,1)))
model.add(Dense(1,activation='sigmoid'))

# Compile & Train
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X,y,epochs=2)