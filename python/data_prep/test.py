from parser_function import read_file
from neighbourhood_functions import return_neighbourhood_matrix

#read_file() function parses a the test.csv file and returns a 
#list of 50,000 values all objects which have a id property, delta property and matrix property
lista = read_file("../data/test.csv")
#Some examples of matrices and ids printed out
print(lista[0].id)
print(lista[0].matrix)

print(lista[1].id)
print(lista[1].matrix)

print(lista[34890].id)
print(lista[34890].matrix)

#return_neighbourhood_matrix() function returns an nxn matrix of 
#the neighbourhood of a single cell within the passed matrix
#parameters are (matrix,n,i,j,size) where n is the size of the neighbourhood and (i,j) is the cell 
neighbour7x7 = return_neighbourhood_matrix(lista[0].matrix,7,0,0,25)
print(neighbour7x7)
