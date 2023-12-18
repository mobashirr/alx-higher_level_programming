#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    i = 0

    while True:
        try:
            if x > i:
                print(my_list[i], end="")
                i += 1
            else:
                print()
                break
        except (r):
            print()
            break
    return i
