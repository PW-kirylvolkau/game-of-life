import csv
import numpy as np

class list_value:
    def __init__(self, id, delta, matrix):
        self.id = int(id)
        self.delta = delta
        self.matrix = matrix

#Creates a matrix from a row
def create_matrix(row, size=25, format=False):
    mat = np.zeros((size,size),dtype=int)
    arr_index = 2 if format else 0
    for i in range(size):
        for j in range(size):
            mat[i,j] = row[arr_index]
            arr_index+=1
    return(mat)

#Reads a csv file and :
#Parameters:
#   filename - name of the file 
#   bsize - number of boards taken from the file
#       if -1: reads all the boards within a file
#   format - specifies if the file is formatted according to the kaggle files
def read_file(filename,bsize=-1,format=False):
    if bsize == -1:
        bsize = board_count(filename)
    if format==True:
        file_list = read_formatted_file(filename,bsize)
    else:
        file_list = read_unformatted_file(filename,bsize)
    return(file_list)

#Reads a file formatted according to kaggle files
#Meaning that the first two rows are for id and delta value   
def read_formatted_file(filename,bsize):
    with open(filename) as fname:
        reader = csv.reader(fname, delimiter=',')
        file_list = [None] * bsize
        line_count = 0
        reader.__next__()
        for row in reader:
            file_list[line_count] = list_value(row[0],row[1],create_matrix(row))
            line_count += 1
            if line_count>=bsize:
                break
    return(file_list)

#reads a file where the format is just row per board
def read_unformatted_file(filename,bsize):
    with open(filename) as fname:
        reader = csv.reader(fname, delimiter=',')
        file_list = [None] * bsize
        line_count = 0
        for row in reader:
            file_list[line_count] = list_value(line_count,0,create_matrix(row,25,False))
            line_count += 1
            if line_count>=bsize:
                break
    return(file_list)

#Returns the amount of rows within a file
def board_count(filename):
    with open(filename) as fname:
        reader = csv.reader(fname, delimiter=',')
        row_count = sum(1 for row in reader)
    return row_count