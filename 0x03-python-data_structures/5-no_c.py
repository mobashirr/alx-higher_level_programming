#!/usr/bin/python3

def no_c(my_string):

    list = [i for i in my_string if i != 'C' and i != 'c']
    str = ""

    for j in list:
        str += j
    return (str)
