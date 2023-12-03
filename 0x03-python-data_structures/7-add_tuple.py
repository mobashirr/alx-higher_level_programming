#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    i = len(tuple_a)
    j = len(tuple_b)

    # set values for cases out of range
    a = tuple_a[0] if i >= 1 else 0
    b = tuple_a[1] if i >= 1 else 0
    a = tuple_a[0] if j >= 1 else 0
    b = tuple_a[1] if j >= 1 else 0

    if i > 1 and j >= 1:
        a = tuple_a[0] + tuple_b[0]
    if i > 2 and j >= 2:
        b = tuple_a[1] + tuple_b[1]

    tuple = (a, b)
    return (tuple)
