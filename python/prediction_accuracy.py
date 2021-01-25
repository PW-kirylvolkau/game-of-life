import numpy as np
from simulation import gameoflife
from simulation import generate
import keras
from predict import runPrediction


def value_classifer(actual,predict,matrix):
    if actual == 1 and predict == 1:
        matrix[0][0] += 1
    if actual == 0 and predict == 0:
        matrix[1][1] += 1
    if actual == 1 and predict == 0:
        matrix[1][0] += 1
    if actual == 0 and predict == 1:
        matrix[0][1] += 1
    return matrix

def calc_accuracy_stats(board, prediction, size, steps=5):
    confusion_m = [[0,0],[0,0]]
    evolved_prediction = prediction
    for i in range(steps):
        evolved_prediction = gameoflife.step(prediction,size)
    print(board)
    print(prediction)
    for i in range(size):
        for j in range(size):
            confusion_m = value_classifer(board[i,j],evolved_prediction[i,j],confusion_m)
    acc = (confusion_m[0][0]+confusion_m[1][1])/(size*size)
    print("Accuracy: ",acc," %")
    precision = confusion_m[0][0]/(confusion_m[0][0]+confusion_m[0][1])
    print("Precision: ",precision)
    recall = confusion_m[0][0]/(confusion_m[0][0]+confusion_m[1][0])
    print("Recall: ",recall)
    f1_score = 2*((precision*recall)/(precision+recall))
    print("F1 Score: ",f1_score)
    specificity = confusion_m[1][1]/(confusion_m[1][1]+confusion_m[0][1])
    print("Specificity: ",specificity)
    print(confusion_m)


#does not work
#path_prefix = "./saved_models/"
#model_paths = [
#        "model11_9crossentropy_100_100.model",
#        "model9_7crossentropy_1000_200.model",
#        "model7_5crossentropy_1000_100.model",
#        "model5_3crossentropy_1000_100.model",
#        "model_crossentropy_1000_1000.model",
#        ]
#models = []
#for path in model_paths:
#    models.append(keras.models.load_model(path_prefix+path))
#
#
#size = 25
#b1 = generate.convertArrayToBoard(generate.generateBoardArray(size),size)
#b2 = gameoflife.runSimulation(b1)
#b3 = runPrediction(b2, models, 25)
#calc_accuracy_stats(b1,b3,size)
