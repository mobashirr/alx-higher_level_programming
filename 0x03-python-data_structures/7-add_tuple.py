#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    i = len(tuple_a)
    j = len(tuple_b)

    # set values for cases out of range
    a = tuple_a[0] if i >= 1 else 0
    b = tuple_a[1] if i >= 2 else 0
    a += tuple_b[0] if j >= 1 else 0
    b += tuple_b[1] if j >= 2 else 0

    tuple = (a, b)
    return (tuple)

'''
# test cases:
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
'''
