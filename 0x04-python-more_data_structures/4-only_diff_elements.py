#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    new = [x for x in set_1 if x not in set_2]
    new += [x for x in set_2 if x not in set_1]
    return new

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))