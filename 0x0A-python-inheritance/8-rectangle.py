#!/usr/bin/python3

import BaseGeometry

"""Module for Rectangle class"""

class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

