from data_prep import parser
import numpy as np
import prediction_accuracy as predacc


def run_board_accuracy(start_fname, predicted_fname,fsize,fformat,bsize=25):
    start_bs = parser.read_file(start_fname,fsize,fformat)
    predicted_bs = parser.read_file(predicted_fname,fsize,fformat)

    for i in range(fsize):
        predacc.calc_accuracy_stats(start_bs[i].matrix,predicted_bs[i].matrix,25)