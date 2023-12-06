#!/usr/bin/python3

def number_keys(a_dictionary):

    num = 0
    for i in a_dictionary:
        num += 1
    return (num)

'''
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level", "new": None}
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
'''
