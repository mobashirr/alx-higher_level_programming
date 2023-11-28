#!/usr/bin/python3

def print_last_digit(number):

    last = number % 10

    if (number < 0):
        last = number % -10
        last *= -1

    print(last, end="")
    return (last)


'''
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
'''
