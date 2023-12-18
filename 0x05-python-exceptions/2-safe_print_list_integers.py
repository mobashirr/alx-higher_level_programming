#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    i = 0
    ex = 0  #we use i as index for list but we only return number of printed char

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except (TypeError, ValueError):
            i += 1
            ex += 1 # we skiped element from the list
        except IndexError:
            break
    print()
    return i - ex