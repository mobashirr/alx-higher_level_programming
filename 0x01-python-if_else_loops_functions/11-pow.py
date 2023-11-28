#!/usr/bin/python3

def pow(a, b):
    
    result = a

    if b == 0:
        return (1)

    if b > 0:
        for _ in range(1, b):
            result *= a
    elif b < 0:
        b *= -1
        result = 1 / result
        for _  in range(1, b + 1):
            result /= 10

    return(result)


pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
