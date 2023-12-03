#!/usr/bin/python3

def no_c(my_string):

    str = "{}".format("".join(i for i in my_string if (i != 'C' and i != 'c')))
    print(str)
    return(str)

