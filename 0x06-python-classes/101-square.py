#!/usr/bin/python3

'''task 101'''


class Square:
    '''task 101'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        res = ""
        if self.__size == 0:
            return '\n'
        else:
            for _ in range(self.__position[1]):
                res += "\n"
            for i in range(self.__size):
                # res += print(" " * self.__position[0] + "#" * self.__size)
                res += " " * self.__position[0]
                res += "#" * self.__size
                res += "\n" if i < self.__size - 1 else ""
        return res

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method to calculate the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method to print the square with position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)


'''
# test case:
my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
'''
