#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for j in range(len(matrix)):
        for k in matrix[j]:
            sep = " " if k != matrix[j][-1] else ""
            print("{:d}".format(k), end="{}".format(sep))
        print("$")
