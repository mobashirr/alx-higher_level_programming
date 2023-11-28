#!/usr/bin/python3

for i in range(97, 122):
    if i not in [101,113]:
        print("{:c}".format(i), end="")
