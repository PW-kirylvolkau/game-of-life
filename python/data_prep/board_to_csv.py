import numpy as np
import csv 

def board_to_csv(board, fname, size=25):
    with open(fname,'w',newline='') as file:
        writer = csv.writer(file)
        arr_index = 0
        tmplist = [None]*(size*size)
        for i in range(size):
            for j in range(size):
                tmplist[arr_index] = board[i,j]
                arr_index += 1 
        writer.writerow(tmplist)

def boards_to_csv(boards, fname, board_count, size=25):
    with open(fname,'w',newline='') as file:
        writer = csv.writer(file)
        for k in range(board_count):
            board = boards[k]
            arr_index = 0
            tmplist = [None]*(size*size)
            for i in range(size):
                for j in range(size):
                    tmplist[arr_index] = board[i,j]
                    arr_index += 1 
            writer.writerow(tmplist)  
