#!/usr/bin/python3
import sys

def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError, NameError) as erorr:
        sys.stderr.write(f"Exception: {erorr}")
        return False
