import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Dense

from data_prep import neighbourhood as nb
from data_prep import train_parser as tp

from cone_models import layer11_9 as lr #change for models
from cone_models import training
import time

full_data = tp.read_file("data/train.csv")

delta1_matrices = [m for m in full_data if int(m.delta) == 1]

train_set = [];
target_set = [];
test_setX = [];
test_setY = [];

print(len(delta1_matrices))

SAMPLE_SIZE = 500
EPOCH_COUNT = 20
INPUT_DIM = 11 #change for models
OUTPUT_DIM = 9 #change for models

c = 1 #counter for splitting data set into training and testing data
flag = True
for m in delta1_matrices:
    if c == SAMPLE_SIZE:
        flag = False;
    if flag:
        for i in range(0,24):
            for j in range(0, 24):
                train_set.append(nb.return_neighbourhood_matrix(m.stopmatrix, INPUT_DIM, i, j, 25))
                target_set.append(nb.return_neighbourhood_matrix(m.stopmatrix, OUTPUT_DIM, i, j, 25))
               # for the 3_1 model
               # train_set.append(nb.return_neighbourhood_matrix(m.stopmatrix, 3, i, j, 25))
               # target_set.append(m.startmatrix[i][j])
        c = c + 1
    else:
        for i in range(0,24):
            for j in range(0, 24):
                test_setX.append(nb.return_neighbourhood_matrix(m.stopmatrix, INPUT_DIM, i, j, 25))
                test_setY.append(nb.return_neighbourhood_matrix(m.stopmatrix, OUTPUT_DIM, i, j, 25))
               # for the 3_1 model
               # test_setX.append(nb.return_neighbourhood_matrix(m.stopmatrix, 3, i, j, 25))
               # test_setY.append(m.startmatrix[i][j])
        c = c + 1
        if c == 2 * SAMPLE_SIZE:
            break

model = lr.get11_9Model() #change for models
print("Starting Training...")
start_time = time.time()
(history, trained) = training.trainModel(model, np.asarray(train_set), np.asarray(target_set), EPOCH_COUNT, True)
print("Training took:", time.time() - start_time)
training.testModel(trained, np.asarray(test_setX), np.asarray(test_setY), True)
model_path = 'saved_models/model11_9mae_500_20.model'
trained.save(model_path)
print("Model Saved to:", model_path)

