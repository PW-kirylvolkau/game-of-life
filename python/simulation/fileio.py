import generate as g
import numpy as np

def createTestFile(boardSize=25, n=10, filename="./data.csv"):
    f = open(filename, "w")
    for i in range(n):
        board = g.generateBoardArray(boardSize)
        line = ''
        for c in board:
            line = line + str(c) + ','
        line = line[:-1] + '\n'
        f.write(line)

def loadTestFile(filename="./data.csv"):
    f = open(filename, "r")
    boards = []
    for line in f.readlines():
        boards.append(np.fromstring(line, dtype=int, sep=','))
    return boards
