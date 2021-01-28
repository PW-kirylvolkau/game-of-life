from tensorflow import keras
from data_prep import neighbourhood as nb
from predict import runPrediction, board_to_csv
from simulation import fileio
from numpy import genfromtxt
from data_prep import parser

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
save_path = "./predicted_iterative.csv"

if opt == 'y':
    print("Please specify path for the board:")
    path = input()
    
print("Loading board: ", path)
board_list = parser.read_file(path)
count = len(board_list)
predicted = [None] * count
for i in range(count):
    board = board_list[i].matrix
    print("Loaded board.")
    print("Running Prediction...")
    predicted[i] = runPrediction(board, models, 25)
    print(predicted[i])
    board_to_csv(predicted[i], 25, save_path)
    print("Prediction over data saved to: ", save_path)

#Prediction Accuracy not added into the function






