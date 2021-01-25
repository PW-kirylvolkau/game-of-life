import csv
import numpy as np

#File for functions to parse test.csv

class train_val:
    def __init__(self, id, delta, startmatrix, stopmatrix):
        self.id = int(id)
        self.delta = delta
        self.startmatrix = startmatrix
        self.stopmatrix = stopmatrix

def create_matrices(row):
    start = np.zeros((25,25))
    stop = np.zeros((25,25))
    arr_index = 2
    for i in range(25):
        for j in range(25):
            start[i,j] = row[arr_index]
            arr_index+=1
    for i in range(25):
        for j in range(25):
            stop[i,j] = row[arr_index]
            arr_index+=1   
    return([start,stop])


#read_file() function parses a the test.csv file and returns a 
#list of 50,000 values all objects which have a id property, delta property and matrix property
#list_value.matrix is a 25x25 matrix containing the values from the .csv file
def read_file(filename,fsize=10000):
    with open(filename) as fname:
        reader = csv.reader(fname, delimiter=',')
        file_list = [None] * fsize
        line_count = 0
        reader.__next__()
        for row in reader:
            if line_count>=fsize:
                break
            matrices = create_matrices(row)
            file_list[line_count] = train_val(row[0],row[1],matrices[0],matrices[1])
            line_count += 1
    return(file_list)
