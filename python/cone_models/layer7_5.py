from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Input
from keras.layers import Activation, Dropout, Dense, Flatten, Reshape

def get7_5Model():
    shape=(7,7,1)
    model = Sequential()
    model.add(Input(shape=(shape)))
    model.add(Conv2D(49, 3, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.add(Reshape((5,5)))
    model.compile(optimizer="sgd", loss='categorical_crossentropy')
    print("Created a model:")
    print(model.summary())
    return model;
