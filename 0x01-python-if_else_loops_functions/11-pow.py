#!/usr/bin/python3

def pow(a, b):
    
    result = a

    if b == 0:
        return (1)

    if b > 0:
        for _ in range(1, b):
            result *= a
    elif b < 0:
        b *= -1
        result = 1 / result
        for _  in range(1, b):
            result /= 10

    return(result)
