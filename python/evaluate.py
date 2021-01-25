from tensorflow import keras
from data_prep import neighbourhood as nb
from predict import runPrediction, board_to_csv
from simulation import fileio
from numpy import genfromtxt
from data_prep import parser
from data_prep import board_to_csv as bcsv
import run_accuracy as runacc

#paths to models to be joined
model_paths = [
        "model11_9crossentropy_100_100.model",
        "model9_7crossentropy_1000_200.model",
        "model7_5crossentropy_1000_100.model",
        "model5_3crossentropy_1000_100.model",
        "model_crossentropy_1000_1000.model",
        ]
print("Loading models...")
path_prefix = "./saved_models/"
models = []
for path in model_paths:
    models.append(keras.models.load_model(path_prefix+path))
print("Loaded models:")
for model in models:
    print(model.summary())

print("Load custom board for prediction (default ./board.csv)? (y/N)")
opt = input();

path = "./board.csv"
save_path = "./predicted_boards.csv"

if opt == 'y':
    print("Please specify path for the board:")
    path = input()

board_list = parser.read_file(path,10,False)
predicted_list = [None] * 10
for i in range(10):
    print("Loading board ",i+1,": ", path)
    board = board_list[i].matrix
    print(board)
    print("Loaded board.")
    print("Running Prediction...")
    predicted = runPrediction(board, models, 25)
    predicted = predicted.astype(int)
    print(predicted)
    predicted_list[i] = predicted
bcsv.boards_to_csv(predicted_list, save_path,10,25)
print("Prediction over data saved to: ", save_path)

print("Running accuracy functions")
runacc.run_board_accuracy("./start_boards.csv",save_path,10,False)







