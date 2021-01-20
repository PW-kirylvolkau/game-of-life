from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Dense

from data_prep import neighbourhood as nb
from data_prep import train_parser as tp

full_data = tp.read_file("data/train.csv")

delta1_matrices = [m for m in full_data if int(m.delta) == 1]

train_set = [];
target_set = [];

print(len(delta1_matrices))

c = 1
for m in delta1_matrices:
    if c == 5:
        break
    for i in range(0,24):
        for j in range(0, 24):
            train_set.append(nb.return_neighbourhood_matrix(m.stopmatrix, 3, i, j, 25))
            target_set.append(m.startmatrix[i][j])
    c = c + 1

print(train_set)
print(target_set)
