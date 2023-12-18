#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        # some cases were value is not int
        # but its a digit so we need to format first
        _value = "{:d}".format(value)
        print(_value)
        return True
    except (TypeError, ValueError, NameError) as erorr:
        sys.stderr.write(f"Exception: {erorr}\n")
        return False
