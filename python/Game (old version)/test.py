from generate import generateBoardArray, convertArrayToBoard, convertBoardToArray
from gameoflife import getNeighbourCount, step
import random


n = 5
#Generates a matrix with random bit values of a given size (default 25)
gameBoard = generateBoardArray(n) #WORKS
#print(gameBoard)
print("\n")
#Function turns array to a working board
board = convertArrayToBoard(gameBoard, n) #WORKS
print(board)
print("\n")
#Function converts board back to an array
arr = convertBoardToArray(board) #WORKS
#print(arr)
print("\n")

#Generate functions work correctly as well as conversion functions

#count Neighbours Testing
size = n

for x in range(2):
    randX = random.randint(0,(size-1))
    randY = random.randint(0,(size-1))
    print("(",randX,",",randY,"): ",getNeighbourCount(randX,randY,board,size)) #WORKS


#Testing step function
board  = step(board,size) #WORKS
print(board)
