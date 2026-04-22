# Experiment 10: CNN
# Aim: Implement simple CNN model

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense

# Dummy data
X = np.random.rand(10,28,28,1)
y = np.random.randint(0,2,10)

# Model
model = Sequential()
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(Flatten())
model.add(Dense(1,activation='sigmoid'))

# Compile & Train
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X,y,epochs=2)