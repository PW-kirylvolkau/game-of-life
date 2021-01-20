from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Dense, Flatten


shape = (3,3)

model = Sequential()
model.add(Flatten(input_shape=shape))
model.add(Dense(9, activation='relu'))
model.add(Dense(1, activation='softmax'))

model.compile()

#model.fit()





