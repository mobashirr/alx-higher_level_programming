#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    len = len(argv)
    print("{0} arguments.".format(len - 1))

    for i in range(1, len):
        print("{:d}: {:s}".format(i, argv[i]))
