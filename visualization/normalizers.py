import numpy as np

def normalize_single(array):
    for i in range(len(array)):
        if array[i] < 0.01:
            array[i] = 0
        else:
            array[i] = 1 
    return array


def recursive_normalize(n_array):
    if n_array.ndim == 1:
        n_array = normalize_single(n_array)
    else:
        for i in range(len(n_array)):
            n_array[i] = recursive_normalize(n_array[i])
    return n_array
