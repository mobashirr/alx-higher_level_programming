#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
           "D": 500, "M": 1000}
    sub = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    res = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in sub:
            res += sub[roman_string[i:i+2]]
            i += 2
        else:
            res += dic[roman_string[i]]
            i += 1

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
