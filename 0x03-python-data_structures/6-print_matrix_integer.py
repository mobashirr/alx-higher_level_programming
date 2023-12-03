#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if not matrix:
        pass
    else:
        for j in range(len(matrix)):
            for k in matrix[j]:
                sep = " " if k != matrix[j][-1] else ""
                print("{:d}".format(k), end="{}".format(sep))
            print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()