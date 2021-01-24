from tensorflow import keras


#paths to models to be joined
model_paths = [
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

if opt == 'y':
    print("Please specify path for the board:")
    path = input()
    
print("Loading board: ", path)
