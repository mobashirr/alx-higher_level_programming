#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    i = len(my_list)

    for j in range(1, i):
        print("{:d}".format(my_list[i - j]))
