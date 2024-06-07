#!/usr/bin/python3

'''rectangle class mod'''


from base import Base


class Rectangle(Base):
    '''rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''assign the values with setter methods'''
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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

    def update(self, *args, **kwargs):
        '''update rectangle'''

        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' return the dictionary representation of the Rectangle'''
        Rectangle_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y }
        return Rectangle_dict


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    r3 = Rectangle(10, 2, 0, 0)
    Rectangle.save_to_file([r1, r2,r3])

    with open("Rectangle.json", "r") as file:
        print(file.read())