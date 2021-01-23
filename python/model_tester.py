from tensorflow import keras

models = [
        "model_crossentropy_1000_100.model",
        "model5_3crossentropy_1000_100.model",
        "model7_5crossentropy_1000_100.model"
        ]

print("Select Model to Investigate:")
model_index = 0;
for m in models:
    print(model_index, ": ", m)
    model_index = model_index + 1

selected = int(input())

model_path = "./saved_models/" + models[selected]
print("Selected Model:", model_path)
print("Loading...")
model = keras.models.load_model(model_path)
print("Loaded Model:")
print(model.summary())
