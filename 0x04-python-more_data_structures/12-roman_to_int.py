#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string:
        return None
    num = roman_string

    dic = {"I":1, "V":5, "X":10, "L":50, "C":100,
           "D":500, "M":1000}
    sub = {"IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    bol = lambda x: True if x in sub else False
    res = 0

    if len(num) > 1 and bol(num):
         return sub[num]

    for i in range(len(roman_string)):
        if roman_string[i] in dic:
                con = num[i]+num[++i]
                --i
                if bol(con):
                    res += sub[con]
                else:
                    res += dic[num[i]]

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
