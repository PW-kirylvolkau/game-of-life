from tensorflow import keras
from data_prep import neighbourhood as nb
from predict import runPrediction
from numpy import genfromtxt
from data_prep import parser
                    

#paths to models to be joined
model_paths = [
        "model11_9croessentropy_100_100.model",
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
board_list = genfromtxt(path, dtype=int, delimiter=',')
board = parser.create_matrix(board_list, size=25, file=False)
print("Loaded board.")
print("Running Prediction...")
predicted = runPrediction(board, models, 25)
#TODO saving the prediction to a file
print("Prediction over data saved to: ", save_path)






