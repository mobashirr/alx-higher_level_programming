#!/usr/bin/python3

'''Why a getter and setter?

Reminder: size is a private attribute.
We did that to make sure we control the type and value.
Getter and setter methods are not 100% Python, but more OOP.
With them, you will be able to validate the assignment of a private attribute
and also define how getting the attribute value will be available
from outside - by copy?
by assignment? etc. Also, adding type/value validation in
the setter will centralize the logic,
 since you will do it in only one place.'''


class Square:
    '''class square'''

    def __init__(self, size=0):
        try:
            if isinstance(size, int) and size >= 0:
                self.size = size
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        except TypeError:
            raise TypeError("size must be an integer")

    '''return the square of etrribute size'''
    def area(self):
        try:
            if isinstance(self.size, int) and self.size >= 0:
                return self.size * self.size
            elif self.size < 0:
                raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        except (TypeError, ValueError):
            raise TypeError("size must be an integer")


'''
# test case:
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
'''
