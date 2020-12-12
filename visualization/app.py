from flask import Flask, render_template, jsonify
import pandas as pd
from random import randint
from csv import reader, writer

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
    with open('example.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_cells = list(csv_reader)

    list_of_cells = list_of_cells[0]
    generate_board()

    return render_template('board.html', list_of_cells = list_of_cells)


if __name__ == '__main__':
    app.run(debug=True)