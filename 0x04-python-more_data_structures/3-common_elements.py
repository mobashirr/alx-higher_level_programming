#!/usr/bin/python3

def common_elements(set_1, set_2):

    new = [x for x in set_1 if x in set_2]
    return (new)


'''
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
'''
