import numpy as np
import joblib as joblib
from sklearn import metrics

import simulation as game
import generate_data as gd
import accuracy

import argparse
import time
import sys
import os 
import csv

###### Data Prediction #######

def predict():
    # add arguments
    parser = argparse.ArgumentParser(description="Predict Conway's game of life initial board")
    parser.add_argument('-m', dest='model', required=True)
    parser.add_argument('-b', dest='one_board', required=False)
    args = parser.parse_args()
    
    if not os.path.exists("models"):
        print("Models do not exist!")
        sys.exit()

    # Parse arguments
    classNum = int(args.model)
    step = 5
    single_board_mode = False
    if args.one_board and int(args.one_board) == 1:
        single_board_mode = True

    # read in  data, parse into training and target sets
    print("\n--------------- START PREDICTION ---------------")
    print ("Reading the testdata...")
    test_start = np.loadtxt(open('Data/test_start.csv','r'), delimiter=',', dtype='int')
    test_end = np.loadtxt(open('Data/test_end.csv','r'), delimiter=',', dtype='int')

    if single_board_mode == True:
        test_start = test_start[12].reshape(1,-1)
        test_end = test_end[12].reshape(1,-1)
        print("----- Initial test board -----")
        print(test_start[0].reshape(20,20))
        print("----- Ending test board -----")
        print(test_end[0].reshape(20,20))

    # Load model
    model_name = ''
    if classNum == 1:
        clf = joblib.load('./models/knc_step_5.sav')
        model_name = 'knc'
    elif classNum == 2:
        clf = joblib.load('./models/mlp_step_5.sav')
        model_name = 'mlp'
    else:
        clf = joblib.load('./models/rfc_step_5.sav')
        model_name = 'rfc'

    # predict the values
    print("Model loaded. Model: ", model_name)
    print("\nPredicting the values for step size = %i" %(step))
    st_prd = time.time()
    prediction = clf.predict(test_end)
    ed_prd = time.time()
    print("Prediction complete. Elasped time = %f s" %(ed_prd-st_prd))
        
    # Save prediction results
    if single_board_mode == False:
        outfile = 'results/prediction_' + model_name + ".txt"
        f = open(outfile, 'w+')
        for item in prediction:
            f.write(','.join([str(x) for x in item]) + '\n')
        f.close()

    ### Calculating F1 score ###
    # Firstly, evolve prediction boards 5 steps forward
    sample_size = 400
    games = 1
    if single_board_mode == False:
        sample_size = prediction.shape[0]*prediction.shape[1]
        games = prediction.shape[0]
        
    evolved_boards = []
    for i in range(games):
        #print(len(prediction[i]))
        board = gd.convertArrayToBoard(prediction[i])
        tmp = game.runSimulation(board,20,5)
        board2 = gd.convertBoardToArray(tmp)
        evolved_boards.append(board2)

    evolved_boards = np.asarray(evolved_boards)

    ##### Calculating Accuracy #####
    # F1 score is unsymmetric between positive and negative cases !
    (TP_1,TN_1,FP_1,FN_1) = accuracy.calculate_confusion_matrix(test_end,evolved_boards,1,0)
    (TP_0,TN_0,FP_0,FN_0) = accuracy.calculate_confusion_matrix(test_end,evolved_boards,0,1)

    print("\n--------- Confusion matrices ----------")
    matrix_0 = np.asarray([TP_0,FP_0,FN_0,TN_0])
    matrix_1 = np.asarray([TP_1,FP_1,FN_1,TN_1])
    print("Positive Class = 1: \n", matrix_1.reshape(2,2))
    print("Positive Class = 0: \n",matrix_0.reshape(2,2))

    print("\n-------------- F1 score ---------------")
    f1_1 = accuracy.calculate_f1_score(TP_1,TN_1,FP_1,FN_1)
    f1_0 = accuracy.calculate_f1_score(TP_0,TN_0,FP_0,FN_0)
    print("F1-Score for Positive Class = 1: {:.3f} %".format(f1_1*100))
    print("F1-Score for Positive Class = 0: {:.3f} %".format(f1_0*100))

    print("\n--- Matthews correlation coefficient---")
    MCC_1 = accuracy.calculate_MCC(TP_1,TN_1,FP_1,FN_1)
    MCC_0 = accuracy.calculate_MCC(TP_0,TN_0,FP_0,FN_0)
    print("MCC for Positive Class = 1: {:.3f} %".format(MCC_1*100))
    print("MCC for Positive Class = 0: {:.3f} %".format(MCC_0*100))
    print("")
    # if single_board_mode == True:
    #     print("\n----- Prediction board -----")
    #     print(prediction[0].reshape(20,20))
    #     print("----- Evolved prediction board -----")
    #     print(evolved_boards[0].reshape(20,20))
    

if __name__ == "__main__":
    predict()