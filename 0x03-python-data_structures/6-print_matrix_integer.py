#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):


	for j in range(len(matrix)):
		for k in matrix[j]:
			print("{:d}".format(k),
		 			end=" " if k !=matrix[j][-1] else "")
		print("$")
