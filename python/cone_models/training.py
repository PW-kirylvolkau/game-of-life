import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Dense, Flatten

def trainModel(model, train_set, target_set, epoch_count=100, expand=False):
    if expand:
        train_set = tf.expand_dims(train_set, axis=-1)
    trained = model.fit(
            train_set,
            target_set,
            epochs=epoch_count
            )
    return (trained, model);

def testModel(model, testX, testY, expand=False):
    if expand:
        testX = tf.expand_dims(testX, axis=-1)
    result = model.evaluate(testX, testY)
    print("Result of testing: ", result)
