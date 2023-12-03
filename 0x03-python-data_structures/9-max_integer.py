#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return (None)
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = int(i)
    return (max)


'''
#test case:
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
'''
