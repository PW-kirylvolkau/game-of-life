import argparse
import numpy as np

def getNeighbourCount(x, y, board, boardSize = 25):
    sum = board[(x-1)%boardSize, (y-1)%boardSize] + \
          board[(x-1)%boardSize, y] + \
          board[(x-1)%boardSize, (y+1)%boardSize] + \
          board[x, (y-1)%boardSize] + \
          board[x, (y+1)%boardSize] + \
          board[(x+1)%boardSize, (y-1)%boardSize] + \
          board[(x+1)%boardSize, y] + \
          board[(x+1)%boardSize, (y+1)%boardSize]
    return sum


def step(board, boardSize = 25):
    copy = board.copy()
    for i in range(boardSize):
        for j in range(boardSize):
            count = getNeighbourCount(i, j, board, boardSize)
            if(count < 2): #underpopulation
                copy[i,j] = 0
            elif((count == 2 or count == 3) and board[i,j] == 1): #statis
                copy[i,j] = 1
            elif(count > 3): #overpopulation
                copy[i,j] = 0
            elif(count == 3 and board[i,j] == 0): #reproduction
                copy[i,j] = 1
    return copy

def runSimulation(board, boardSize=20, steps=5):
    for i in range(steps):
    	board = step(board, boardSize)

