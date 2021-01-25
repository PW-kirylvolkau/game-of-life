import numpy as np
import math

def calculate_confusion_matrix(test_data, prediction, positiveClass=1, negativeClass=0):
    games = prediction.shape[0]
    cells = prediction.shape[1]
    TN = 0; TP = 0; FP = 0; FN = 0
    for i in range(games):
        for j in range(cells):
            if test_data[i][j] == prediction[i][j] == positiveClass:
                TP += 1
            if test_data[i][j] == prediction[i][j] == negativeClass:
                TN += 1
            if test_data[i][j] == negativeClass and prediction[i][j] == positiveClass:
                FP += 1
            if test_data[i][j] == positiveClass and prediction[i][j] == negativeClass:
                FN += 1
    return TP,TN,FP,FN


def calculate_f1_score(TP, TN, FP, FN, weight=1):
    if (TP + FP) == 0:
        return 0
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = (1 + weight**2) * ((precision * recall)/((weight**2 * precision) + recall))
    return f1


# Matthews correlation coefficient
def calculate_MCC(TP, TN, FP, FN):
    if (TP + FP) == 0 or (TP + FN) == 0 or (TN + FP) == 0 or (TN + FN) == 0:
        denominator = 1
    else:
        denominator = math.sqrt((TP + FP)*(TP + FN)*(TN + FP)*(TN + FN))
    MCC = ((TP*TN) - (FP*FN)) / denominator
    return MCC