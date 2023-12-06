#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string:
        return None

    dic = {"I":1, "V":5, "X":10, "L":50, "C":100,
           "D":500, "M":1000}
    res = 0

    for i in range(len(roman_string)):
        if roman_string[i] in dic:
                res += dic[roman_string[i]]

    return res

'''
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
'''
