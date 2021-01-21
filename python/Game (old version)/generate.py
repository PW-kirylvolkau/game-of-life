import random
import numpy as np

def generateBoardArray(boardSize = 20):
    return np.asarray([random.randint(0,1) for _ in range(boardSize**2)])

def convertBoardToArray(board = np.matrix([])):
    return board.A1

def convertArrayToBoard(arr = [], boardSize = 20):
    def subArrays(a,n):
            for i in range(0, len(a), n):
                yield a[i:i + n]

    return np.asmatrix(list(subArrays(arr, boardSize)))
