from simulation import generate as g
from simulation import gameoflife as gol
from data_prep import board_to_csv as csvwriter
#Generate list of boards of random values 
amount = 10
boards = [None] * amount
for i in range(amount):
    boards[i] = g.convertArrayToBoard(g.generateBoardArray())
    #print(boards[i])

evovled_boards = boards
#Evolve the boards 5 steps
for i in range(amount):
    for j in range(5):
        evovled_boards[i] = gol.step(evovled_boards[i])

#write to files
csvwriter.boards_to_csv(boards,"./start_boards.csv",amount)
csvwriter.boards_to_csv(evovled_boards,"./end_boards.csv",amount)

