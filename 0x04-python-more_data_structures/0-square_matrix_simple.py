#!/usr/bin/python3
from math import pow
def square_matrix_simple(matrix=[]):

    list = [[],[],[]]
    for i in range(0,len(matrix)):
        list[i] = [int(pow(x,2)) for x in matrix[i]]
    return (list)

'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
'''