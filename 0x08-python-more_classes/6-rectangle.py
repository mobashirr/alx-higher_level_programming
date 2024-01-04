#!/usr/bin/python3

''' class Rectangle '''


class Rectangle:
    '''class Rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return (self.__height)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        res = (self.__height * 2) + (self.__width * 2)
        if self.__height > 0 and self.__width > 0:
            return res
        else:
            return 0

    def __str__(self):
        res = ""

        for x in range(self.__height):
            for y in range(self.__width):
                res += "#"
            if x + 1 != self.__height:
                res += '\n'
        return res

    def __repr__(self) -> str:
        res = f"Rectangle(width={self.__width}, height={self.__height})"
        return res

    def __del__(self):
        # this method called when object deleted
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1