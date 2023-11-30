#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    len = len(argv)
    cont = 0

    for i in range(1, len):
        cont += int(argv[i])
    print(cont)
