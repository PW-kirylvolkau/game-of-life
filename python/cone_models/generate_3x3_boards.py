import itertools
from data_prep import parser

n = 9
lst = [list(i) for i in itertools.product([0, 1], repeat=n)]

matrix_list = []
for l in lst:
    matrix_list.append(parser.create_matrix(l, size=3, file=False))

print(matrix_list[21])

