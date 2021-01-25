from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Input
from keras.layers import Activation, Dropout, Dense, Flatten, Reshape

def get11_9Model():
    shape=(11,11,1)
    model = Sequential()
    model.add(Input(shape=(shape)))
    model.add(Dense(81, activation='relu'))
    model.add(Conv2D(64, 3, activation='relu'))
    #model.add(Dense(81, activation='relu'))
    model.add(Conv2D(32, 1, activation='relu'))
    #model.add(Dense(81, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    #model.add(Reshape((9,9)))
    model.compile(optimizer="sgd", loss='mean_absolute_error')
    print("Created a model:")
    print(model.summary())
    return model
