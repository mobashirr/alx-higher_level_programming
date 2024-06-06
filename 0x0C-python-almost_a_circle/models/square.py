#!/usr/bin/python3

from rectangle import Rectangle

class Square(Rectangle):
    
    def __init__(self, size, x=0, y=0, id=None):
        '''assign the values with setter methods'''
        super().__init__(size, size, x, y, id)
 
    def __str__(self):
        '''return the string representation of the object'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)
