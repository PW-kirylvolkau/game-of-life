import numpy as np
import joblib as joblib
from sklearn.ensemble import RandomForestClassifier 
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.neural_network import MLPClassifier
from sklearn import metrics

import time
import pdb
import sys
import gc
import os 
import csv


def train_models():
    # prepare the directories
    if not os.path.exists("results"):
        os.mkdir("results")
    if not os.path.exists("models"):
            os.mkdir("models")

    if len(sys.argv) != 2:
        print("Wrong number of arguments!!")
        sys.exit()

    arglist = sys.argv
    classNum = int(arglist[1])
    step = 5
    
    # read in data, parse into training and target sets
    print("\nReading the traindata...")
    traindata = np.loadtxt(open('Data/train.csv','r'), skiprows=1, delimiter=',', dtype='int')
    n_train, m_train = traindata.shape

    # clean up the traindata
    print("Extracting the traindata...")
    id = traindata[:,0]
    delta = traindata[:,1]

    train_start = np.array(traindata[traindata[:, 1] == step, 2:402], dtype=int)
    train_end = np.array(traindata[traindata[:, 1] == step, 402:802], dtype=int)
    print(np.shape(train_start))

    # Training models
    model_name = ''
    if classNum == 1:
        clf = KNeighborsClassifier(n_neighbors=15,weights='distance')
        model_name = 'knc'
    elif classNum == 2:
        clf = MLPClassifier(max_iter=1000)
        model_name = 'mlp'
    else:
        clf = RandomForestClassifier(n_estimators=100, n_jobs=1)
        model_name = 'rfc'

    print("\nRunnning the fit for step size = {0:d}, model: {}".format(step,model_name))
    st_clf = time.time()
    #clf = MLPClassifier(max_iter=1000, random_state=1)
    clf.fit(train_end, train_start)
    ed_clf = time.time()
    print("Fit complete. elapsed time = %f s" %(ed_clf-st_clf))
    
    # save the clf
    print("Saving the model for step size = %i" %(step))
    savedir = 'models' 
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    savefile = savedir + "/" + model_name + "_step_" + str(step) + ".sav"
    joblib.dump(clf, savefile) 



if __name__ == "__main__":
    train_models()





