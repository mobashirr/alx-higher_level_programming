#!/usr/bin/python3

'''this module contain function to return addtion of int'''

def add_integer(a, b=98):
    '''
    This function adds two int.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The s
    '''

    if not isinstance(a,int) and not isinstance(a,float):
        raise TypeError("a must be an integer")
    elif not isinstance(b,int) and not isinstance(b,float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
