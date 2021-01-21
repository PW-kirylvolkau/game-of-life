from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Dense, Flatten

def get3_1Model():
    shape = (3,3)
    model = Sequential()
    model.add(Flatten(input_shape=shape))
    model.add(Dense(9, activation='relu'))
    model.add(Dense(1, activation='relu'))
    model.compile(loss='mean_absolute_error')
    print("Created a model:")
    print(model.summary())
    return model;


def trainModel(model, train_set, target_set):
    trained = model.fit(
            train_set,
            target_set,
            epochs=2
            )
    return (trained, model);

def testModel(model, testX, testY):
    result = model.evaluate(testX, testY)
    print(result)




