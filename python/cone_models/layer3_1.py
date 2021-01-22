from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Dense, Flatten

def get3_1Model():
    shape = (3,3)
    model = Sequential()
    model.add(Flatten(input_shape=shape))
    model.add(Dense(9, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer="sgd" ,loss='binary_crossentropy')
    print("Created a model:")
    print(model.summary())
    return model;
