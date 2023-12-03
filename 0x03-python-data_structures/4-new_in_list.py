#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    i = len(my_list) - 1
    new = [e for e in my_list]

    if idx > i or idx < 0:
        return (new)

    new[idx] = element 
    return(new)
