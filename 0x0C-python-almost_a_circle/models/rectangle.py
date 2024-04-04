#!/usr/bin/python3

'''rectangle class mod'''


from base import Base


class Rectangle(Base):
    '''rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(Self):
        '''height getter'''
        return Self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def display(self):
        '''display rectangle'''

        for _ in range(self.y):
            '''handle y'''
            print()

        for i in range(self.height):
            '''handle height'''

            for _ in range(self.x):
                '''handle x'''
                print(' ', end='')

            for _ in range(self.width):
                '''handle width'''
                print('#', end='')
            print()

    def area(Self):
        '''area of rectangle'''
        res = Self.width * Self.height
        return res

    def __str__(self):
        '''string representation'''
        rep = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return rep

r1 = Rectangle(2, 3, 2, 2)
r1.display()
print("---")
r2 = Rectangle(3, 2, 1, 0)
r2.display()