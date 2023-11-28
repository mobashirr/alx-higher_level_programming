#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i + 1, 10):
        # this way no duplcated couple will shown
	#also no sep at the end
        print("{:d}{:d}".format(i, j), end=", " if i != 8 else "\n", flush=True)
