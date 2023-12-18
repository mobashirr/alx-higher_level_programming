#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ''' pritn first x elements of my_list: '''
    count = 0

    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError:
        pass

    print()  # Print a newline after all integers
    return count


'''
def safe_print_list_integers(my_list=[], x=0):

    i = 0   #i is idx for list
    ex = 0   #but we only return num of printed elements

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            ex += 1  # we skipped an element from the list
        except IndexError:
            break
        i += 1

    print()
    return i - ex
'''
