#!/usr/bin/python3

'''base class mod'''

class base():
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = base.__nb_objects
