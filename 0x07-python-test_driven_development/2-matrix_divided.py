#!/usr/bin/python3

''' moduele contain matrix_divided func'''


def matrix_divided(matrix, div):
    '''
    this func divide all the matrix elements by div
    
    Parameters:
    matrix list of list of int or float
    div the divtion number

    Returns:
    new matrix with divided elements with same size
    '''

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise TypeError("division by zero")
    elif len(matrix) <= 0:
        return

    first_row = len(matrix[0])

    # Shallow copy:
    new = [ele[:] for ele in matrix]

    for row in new:
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(row)):
            if not isinstance(row[i], int) and not isinstance(row[i], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row[i] = round(row[i] / div, 2)

    return new

'''
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
'''