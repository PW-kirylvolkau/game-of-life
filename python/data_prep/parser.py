import csv
import numpy as np

class list_value:
    def __init__(self, id, delta, matrix):
        self.id = int(id)
        self.delta = delta
        self.matrix = matrix

def create_matrix(row, size=25, file=True):
    mat = np.zeros((size,size),dtype=int)
    arr_index = 2 if file else 0
    for i in range(size):
        for j in range(size):
            mat[i,j] = row[arr_index]
            arr_index+=1
    return(mat)

def read_file(filename,bsize=10000,format=True):
    if format==True:
        file_list = read_formatted_file(filename,bsize)
    else:
        file_list = read_unformatted_file(filename,bsize)
    return(file_list)
        
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