from flask import Flask, render_template, jsonify, request, redirect
import pandas as pd
from random import randint
from csv import reader, writer
import numpy as np
from prediction import accuracy,predict

#### game of life implementation

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


#### flask app implementation

app = Flask(__name__)

def generate_board():
    result = ''
    for i in range(0,400):
        result += f'{randint(0,1)},'
    result = result[:len(result)-1]
    with open('example.csv', 'w') as write_obj:
        write_obj.write(result)

######

@app.route('/board')
def board():
    with open('start_board.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    list_of_cells = list_of_cells[0]
    # generate_board()
    return render_template('board.html', list_of_cells = list_of_cells)


# Empty board to select fields
@app.route('/start')
def start():
    return render_template('start.html')


# save board from /start_endpoint
@app.route('/save_board', methods=['POST'])
def save_board():
    list_of_cells = request.json['list_of_cells']
    result = ''
    for i in range(0,400):
        if i in list_of_cells:
            result += '1,'
        else:
            result += '0,'
    result = result[:len(result)-1]
    with open('start_board.csv', 'w') as write_obj:
        write_obj.write(result)
    return 'success', 200


# evolve board by 5 steps
@app.route('/evolve')
def evolve():
    with open('start_board.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    list_of_cells = list_of_cells[0]
    list_2d = []
    row = []
    for i in range(0,400):
        row.append(int(list_of_cells[i]))
        if (i+1)%20 == 0:
            list_2d.append(row)
            row = []
    list_2d = np.array(list_2d)
    for i in range(0,5):
        list_2d = step(list_2d, 20)

    result = ''
    for i in list_2d:
        for j in i:
            result += f'{j},'
    result = result[:len(result)-1]
    with open('end_board.csv', 'w') as write_obj:
        write_obj.write(result)

    return redirect('/end_board')
    

# display evolved board
@app.route('/end_board')
def end_board():
    with open('end_board.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    list_of_cells = list_of_cells[0]
    # generate_board()
    return render_template('end_board.html', list_of_cells = list_of_cells)


# predict board state 5 steps before
@app.route('/predict')
def prediction():
    
    test_end = np.loadtxt(open('end_board.csv','r'), delimiter=',', dtype='int')
    # with open('end_board.csv', 'r') as read_obj:
    #     csv_reader = reader(read_obj)
    #     list_of_cells = list(csv_reader)
    # list_of_cells = list_of_cells[0]

    # Tutaj musisz przewidzieć predicted_cells za pomoca swojego modelu i wrzucić to do predicted_board.csv doklaadnie tak jak wyzej
    # np generate_board()
    prediction = predict.one_board(test_end)
    print(prediction)
    result = ''
    for p in prediction:
        result += f'{p},'
    result = result[:len(result)-1]
    with open('predicted_board.csv', 'w') as write_obj:
        write_obj.write(result)
    return redirect('/final')


# display final view
@app.route('/final')
def final():
    with open('start_board.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    start = list_of_cells[0]
    with open('predicted_board.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    predicted = list_of_cells[0]
    # compare start and predicted board
    diffs = []
    for i in range(0,400):
        if start[i] != predicted[i]:
            diffs.append(i)
    print(diffs)
    return render_template('final.html', start=start, predicted=predicted, diffs=diffs)


# Start
if __name__ == '__main__':
    app.run(debug=True)
