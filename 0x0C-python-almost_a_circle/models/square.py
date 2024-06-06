#!/usr/bin/python3

from rectangle import Rectangle

class Square(Rectangle):
    
    def __init__(self, size, x=0, y=0, id=None):
        '''assign the values with setter methods'''
        super().__init__(size, size, x, y, id)
 
    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''        
        self.width = value

    def __str__(self):
        '''return the string representation of the object'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)


    def update(self, *args, **kwargs):
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i,value in enumerate(args):
                if i < len(args):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
