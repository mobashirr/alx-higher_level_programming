#!/usr/bin/python3

def islower(c):

    result = False
    i = f"{c:d}"

    for j in range(97, 123):
        if i == j:
            return(True)

    return(result)