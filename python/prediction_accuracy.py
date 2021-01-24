import numpy as np
from simulation import gameoflife
from simulation import generate
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


size = 25
b1 = generate.convertArrayToBoard(generate.generateBoardArray(size),size)
b2 = generate.convertArrayToBoard(generate.generateBoardArray(size),size)
calc_accuracy_stats(b1,b2,size)