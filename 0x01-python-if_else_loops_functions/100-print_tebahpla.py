#!/usr/bin/python3

for i in range(1, 27):
    print("{:c}".format(123 - i if i % 2 != 0 else 91 - i), end="")
