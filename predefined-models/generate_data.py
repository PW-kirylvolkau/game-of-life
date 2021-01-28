import random
import argparse
import os
import numpy as np
import simulation as game

# setting up the values for the grid
ON = 1
OFF = 0
vals = [ON, OFF]

# Generating functions
def randomGrid(N):
    return np.random.choice(vals, N*N, p=[0.15, 0.85]).reshape(N, N)

def generateBoardArray(boardSize = 20):
    return np.asarray([random.randint(0,1) for _ in range(boardSize**2)])

# Converting functions
def convertBoardToArray(board = np.matrix([])):
    return board.flatten()

def convertArrayToBoard(arr = [], boardSize = 20):
    return np.reshape(arr,(boardSize,boardSize))
   

#### Generate Board and Save to File ####

def createTestFiles(boardSize = 20, n = 100, steps = 5):
    fstart = open("./Data/test_start.csv", "w+")
    endfile = "./Data/test_end.csv"
    fend = open(endfile, "w+")
    for i in range(n):
        # Starting board - evolve random grid 5 steps to be more "probable"
        board = randomGrid(boardSize)
        board = game.runSimulation(board,20,steps)
        startboard = convertBoardToArray(board)
        line = ''
        for c in startboard:
            line = line + str(c) + ','
        line = line[:-1] + '\n'
        fstart.write(line)

        # Ending board
        endboard = game.runSimulation(board,20,steps)
        board = convertBoardToArray(endboard)
        eline = ''
        for c in board:
            eline = eline + str(c) + ','
        eline = eline[:-1] + '\n'
        fend.write(eline)


def loadTestFile(filename):
    f = open(filename, "r")
    boards = []
    for line in f.readlines():
        boards.append(np.fromstring(line, dtype=int, sep=','))
    return boards

def saveBoard(board,filename="./boards.csv"):
    f = open(filename, "a")
    line = ''
    for c in board:
        line = line + str(c) + ','
    line = line[:-1] + '\n'
    f.write(line)



if __name__ == "__main__":
    createTestFiles(20,100,5)