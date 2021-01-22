import numpy as np
import math
from prediction.simulation import runSimulation
import prediction.generate_data as gd

# Return tuple of true positive/negative, false positive/negative
def calculate_confusion_matrix(test_data, prediction, positiveClass, negativeClass):
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

# Calculate F1 score 
def calculate_f1_score(TP, TN, FP, FN, weight=1):
    if (TP + FP) == 0:
        return 0
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    #print("TP: {} | FP: {} | FN: | {}".format(TP, FP, FN))
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


# Return accuracy statistics, test_data - ending board to compare with evolved prediction
def accuracy_results(test_data, prediction):
    ### Calculating F1 score ###
    # Firstly, evolve prediction boards 5 steps forward
    if not isinstance(prediction,np.ndarray) or not isinstance(test_data,np.ndarray):
        prediction = np.asarray(prediction)
        test_data = np.asarray(test_data)
    games = 1
    if prediction.ndim > 1:
        games = prediction.shape[0]
    if prediction.ndim == 1:
        prediction = prediction.reshape(1,-1)
        test_data = test_data.reshape(1,-1)
        
    evolved_boards = []
    for i in range(games):
        board = gd.convertArrayToBoard(prediction[i])
        tmp = runSimulation(board,20,5)
        board2 = gd.convertBoardToArray(tmp)
        evolved_boards.append(board2)

    evolved_boards = np.asarray(evolved_boards)

    ##### Calculating Accuracy #####
    # F1 score is unsymmetric between positive and negative cases !
    (TP_1,TN_1,FP_1,FN_1) = calculate_confusion_matrix(test_data,evolved_boards,1,0)
    (TP_0,TN_0,FP_0,FN_0) = calculate_confusion_matrix(test_data,evolved_boards,0,1)

    print("\n--------- Confusion matrices ----------")
    matrix_0 = np.asarray([TP_0,FP_0,FN_0,TN_0])
    matrix_1 = np.asarray([TP_1,FP_1,FN_1,TN_1])
    print("Positive Class = 1: \n", matrix_1.reshape(2,2))
    print("Positive Class = 0: \n",matrix_0.reshape(2,2))

    print("\n-------------- F1 score ---------------")
    f1_1 = calculate_f1_score(TP_1,TN_1,FP_1,FN_1)
    f1_0 = calculate_f1_score(TP_0,TN_0,FP_0,FN_0)
    print("F1-Score for Positive Class = 1: {:.3f} %".format(f1_1*100))
    print("F1-Score for Positive Class = 0: {:.3f} %".format(f1_0*100))

    print("\n--- Matthews correlation coefficient---")
    MCC_1 = calculate_MCC(TP_1,TN_1,FP_1,FN_1)
    MCC_0 = calculate_MCC(TP_0,TN_0,FP_0,FN_0)
    print("MCC for Positive Class = 1: {:.3f} %".format(MCC_1*100))
    print("MCC for Positive Class = 0: {:.3f} %".format(MCC_0*100))
    print("")

    return matrix_1, matrix_0, f1_1, f1_0, MCC_1, MCC_0
    