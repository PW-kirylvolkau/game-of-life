import numpy as np
import math

def return_neighbourhood_matrix(matrix,n,i,j,size):
    if n>size:
        print("Such neighbourhood is not possible")
        return None
    if i<0 or i>size or j<0 or j>size:
        print("Invalid cell positions (i,j)")
        return None
    level = math.floor(n/2)
    boundi = i + size - level
    boundj = j + size - level
    full = return_extended_matrix(matrix)
    neighbourmat = np.zeros((n,n))
    for k in range(0,n):
        for l in range(0,n):
            neighbourmat[k,l] = full[k+boundi,l+boundj]
    return neighbourmat

def return_extended_matrix(matrix):
    hmat = np.concatenate((matrix,matrix,matrix),1)
    return np.concatenate((hmat,hmat,hmat),0)
