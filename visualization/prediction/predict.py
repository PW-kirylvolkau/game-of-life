import numpy as np
import joblib as joblib
from sklearn import metrics
from prediction.accuracy import accuracy_results

import argparse
import time
import sys
import os 
import csv

###### Data Prediction #######
# Predict initial state of single board
def one_board(end_board,model=2):
    if not os.path.exists("./prediction/models"):
        print("Models do not exist!")
        sys.exit()

    # Prepare variables
    classNum = model
    step = 5
    end_board = end_board.reshape(1,-1)

    # Load model
    model_name = ''
    if classNum == 1:
        clf = joblib.load('./prediction/models/knc_step_5.sav')
        model_name = 'knc'
    else:
        clf = joblib.load('./prediction/models/mlp_step_5.sav')
        model_name = 'mlp'

    # Predict the values
    print("Model loaded. Model: ", model_name)
    print("\nPredicting the values for step size = %i" %(step))
    st_prd = time.time()
    prediction = clf.predict(end_board)
    ed_prd = time.time()
    print("Prediction complete. Elasped time = %f s" %(ed_prd-st_prd))
        
    return prediction[0]
