#!/usr/bin/python3

'''print_square module'''


def print_square(size):
    '''print_square function'''

    if not isinstance(size, int) and not isinstance(size, float):
        return
    elif isinstance(size,float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()

