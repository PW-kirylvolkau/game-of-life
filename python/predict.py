import numpy as np
import tensorflow as tf
from tensorflow import keras
from data_prep import neighbourhood as nb

def runPrediction(board, models, size):
    predicted = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            #for each cell(i,j) run prediction
            #get 11x11 neighbour hood
            input_neigh = nb.return_neighbourhood_matrix(board, 9, i, j, size)
            input_neigh = tf.expand_dims(input_neigh, axis=-1)
            input_neigh = tf.expand_dims(input_neigh, axis=0)
            counter = 1
            for model in models:
                print("Predicting Model ", counter)
                input_neigh = model(input_neigh)
                counter = counter + 1
            predicted[i,j] = 0 if input_neigh < 0.0159652 else 1
    return predicted
