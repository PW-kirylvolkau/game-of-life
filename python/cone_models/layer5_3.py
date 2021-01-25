from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Input
from keras.layers import Activation, Dropout, Dense, Flatten, Reshape

def get5_3Model():
    shape=(5,5,1)
    model = Sequential()
    model.add(Input(shape=(shape)))
    model.add(Conv2D(32, 3, activation='relu'))
    model.add(Dense(9, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.add(Reshape((3,3)))
    model.compile(optimizer="sgd", loss='categorical_crossentropy')
    print("Created a model:")
    print(model.summary())
    return model;
