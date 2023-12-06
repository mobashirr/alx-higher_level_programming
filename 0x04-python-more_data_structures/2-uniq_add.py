#!/usr/bin/python3

def uniq_add(my_list=[]):

    new = [0]
    for i in my_list:
        if i not in new[1:]:
            new.append(i)
            new[0] = new[0] + i
    return(new[0])


'''
#test case:
un = [1, 2, 3, 1, 4, 2, 5]
uniq_add(un)
'''