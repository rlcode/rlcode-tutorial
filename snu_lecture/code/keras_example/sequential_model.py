from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import Adam
import numpy as np

state_size = 15
action_size = 5
batch_size = 100

x_train = np.random.rand(batch_size, state_size)
y_train = np.random.rand(batch_size, action_size)

model = Sequential()
model.add(Dense(30, input_dim=state_size, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(action_size, activation='linear'))
model.compile(loss='mse', optimizer=Adam(lr=0.001))
model.summary()

model.fit(x_train, y_train, batch_size=32, epochs=1)
