#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    len = len(argv)
    cont = "arguments." if len - 1 == 0 else "arguments:"
    print("{:d} {}".format(len - 1, cont))

    for i in range(1, len):
        print("{:d}: {}".format(i, argv[i]))
