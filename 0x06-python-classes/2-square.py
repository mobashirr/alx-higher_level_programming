#!/usr/bin/python3

'''Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0)
size must be an integer, otherwise raise a TypeError exception
with the message size must be an integer
if size is less than 0, raise a ValueError
 exception with the message size must be >= 0
You are not allowed to import any module'''


class Square:
    '''class for square'''

    def __init__(self, size=0) -> None:
        try:
            if isinstance(size, int) and size >= 0:
                self.__size = size
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        except TypeError:
            raise TypeError("size must be an integer")



my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)