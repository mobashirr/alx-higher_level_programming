#!/usr/bin/python3

for i in range(100):
    #we use cnditional expretion
    #in order to ensure last digit with no sepreate
    #and :02d ensure the format is only two digits
    print("{:02d}".format(i), end=", " if i < 99 else "\n", flush=True)
