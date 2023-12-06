#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    list = [row[:] for row in matrix]

    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            list[i][j] = column * column
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
