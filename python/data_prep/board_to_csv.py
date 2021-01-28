import numpy as np
import csv 

def board_to_csv(board, size, fname):
    with open(fname,'w',newline='') as file:
        writer = csv.writer(file)
        tmplist = [None]*(size*size)
        arr_index = 0
        for i in range(size):
            for j in range(size):
                tmplist[arr_index] = board[i][j]
                arr_index+=1
        writer.writerow(tmplist)