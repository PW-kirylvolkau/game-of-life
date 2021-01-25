from data_prep import parser
import numpy as np
import normalizers as norms
import tensorflow as tf
from tensorflow import keras
from data_prep import neighbourhood as nb
import csv

def normalize_tensor(tensorobject):
    tensor_array = tensorobject.numpy()
    tensor_array = norms.recursive_normalize(tensor_array)
    modified_tensor = tf.convert_to_tensor(tensor_array, dtype=tf.int32)
    return modified_tensor


def runPrediction(board, models, size):
    predicted = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            #for each cell(i,j) run prediction
            #get 11x11 neighbour hood
            input_neigh = nb.return_neighbourhood_matrix(board, 11, i, j, size)
            input_neigh = tf.expand_dims(input_neigh, axis=-1)
            input_neigh = tf.expand_dims(input_neigh, axis=0)
            counter = 1
            for model in models:
                input_neigh = model(input_neigh)
                if counter != 5:
                    input_neigh = normalize_tensor(input_neigh)
                counter = counter + 1
            predicted[i,j] = 0 if input_neigh < 0.5 else 1
    return predicted

def board_to_csv(board, size, fname):
    with open(fname,'w',newline='') as file:
        writer = csv.writer(file)
        tmplist = [None]*(size*size)
        arr_index = 0
        for i in range(size):
            for j in range(size):
                tmplist[arr_index] = board[i][j]
                arr_index+=1
        writer.writerow(tmplist)

def predict2(in_path = "./end_board.csv", out_path = "./predicted_board3.csv"):
    board_list = np.genfromtxt(in_path, dtype=int, delimiter=',')
    board = parser.create_matrix(board_list, size=20, file=False)
    path_prefix = "./saved_models/"
    model_paths = [
            "model11_9crossentropy_100_100.model",
            "model9_7crossentropy_1000_200.model",
            "model7_5crossentropy_1000_100.model",
            "model5_3crossentropy_1000_100.model",
            "model_crossentropy_1000_1000.model",
            ]
    models = []
    for path in model_paths:
        models.append(keras.models.load_model(path_prefix+path))
    predicted = runPrediction(board, models, 20)
    board_to_csv(predicted, 20, out_path)
