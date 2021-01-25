from flask import Flask, render_template, jsonify, request, redirect
import pandas as pd
from random import randint
from csv import reader, writer
import numpy as np
from prediction import accuracy,predict
from torch import nn, optim, from_numpy, reshape, save, load
from torch.autograd import Variable


####
def predict_whole():
    with open('end_board.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    list_of_cells = list_of_cells[0]
    list_2d = []
    temp = []
    for c in list_of_cells:
        if int(c) % 20 == 0:
            list_2d.append(temp)
        temp.append(int(c))
    model = load('./model/model2')
    model.eval()
    board = np.array(list_2d)
    list_inputs = []
    temp = []
    for row in range(20):
        for column in range(20):
            for i in range(-5, 6):
                for j in range(-5,6):
                    temp_col = column - i
                    temp_row = row - j
                    if temp_col < 0:
                        temp_col += 20
                    if temp_row < 0:
                        temp_row += 20
                    if temp_col > 19:
                        temp_col -= 20
                    if temp_row > 19:
                        temp_row -= 20
                    temp.append(board[temp_row, temp_col])
            list_inputs.append(temp)
            temp = []
    predicted = []
    for l in list_inputs:
        li = np.array([l])
        li = li.astype('float')
        li = from_numpy(li)
        li = Variable(li)
        output = model(li.float())
        if output.item() >= 0.5:
            predicted.append(1)
        else:
            predicted.append(0)
    result = ''
    for i in predicted:
        result += f'{i},'
    result = result[:len(result)-1]
    with open('predicted3.csv', 'w') as write_obj:
        write_obj.write(result)

    


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
    prediction = predict.one_board(test_end)
    result = ''
    for p in prediction:
        result += f'{p},'
    result = result[:len(result)-1]
    with open('predicted_board.csv', 'w') as write_obj:
        write_obj.write(result)
    # evolve prediction
    with open('predicted_board.csv', 'r') as read_obj:
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
    with open('prediction_evolution.csv', 'w') as write_obj:
        write_obj.write(result)
    # # # #
    prediction = predict.one_board(test_end, 1)
    result = ''
    for p in prediction:
        result += f'{p},'
    result = result[:len(result)-1]
    with open('predicted_board2.csv', 'w') as write_obj:
        write_obj.write(result)
    # evolve prediction
    with open('predicted_board2.csv', 'r') as read_obj:
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
    with open('prediction_evolution2.csv', 'w') as write_obj:
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
    with open('end_board.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    end_board = list_of_cells[0]
    with open('prediction_evolution.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    prediction_evolution = list_of_cells[0]
    with open('predicted_board2.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    predicted2 = list_of_cells[0]
    with open('prediction_evolution2.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)
    prediction_evolution2 = list_of_cells[0]
    # compare start and predicted board
    diffs = [[], [], [], []]
    for i in range(0,400):
        if start[i] != predicted[i]:
            diffs[0].append(i)
        if end_board[i] != prediction_evolution[i]:
            diffs[1].append(i)
        if start[i] != predicted2[i]:
            diffs[2].append(i)
        if end_board[i] != prediction_evolution2[i]:
            diffs[3].append(i)
    # accuracy
    end_2d = []
    predict_2d1 = []
    predict_2d2 = []
    for i in range(0,400):
        end_2d.append(int(end_board[i]))
        predict_2d1.append(int(prediction_evolution[i]))
        predict_2d2.append(int(prediction_evolution2[i]))
    acc1 = accuracy.accuracy_results(end_2d, predict_2d1)
    acc2 = accuracy.accuracy_results(end_2d, predict_2d2)
    return render_template('final.html', start=start, predicted=predicted, diffs=diffs, end_board=end_board, prediction_evolution=prediction_evolution,
    predicted2=predicted2, prediction_evolution2=prediction_evolution2, acc1=acc1, acc2=acc2)


# Start
if __name__ == '__main__':
    app.run(debug=True)
