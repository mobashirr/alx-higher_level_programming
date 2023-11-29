#!/usr/bin/python3

def islower(c):

    result = False

    if (c == ""):
        return (result)
    i = int.from_bytes(c.encode('utf-8'), 'big')

    for j in range(97, 123):
        if i == j:
            return (True)

    return (result)


'''
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
print("notiong is {}".format("lower" if islower("") else "upper"))
'''
