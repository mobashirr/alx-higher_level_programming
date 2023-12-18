#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res = []
    i = 0
    out_range = False

    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
            res.append(div)
        except IndexError:
            res.append(0)
            out_range = True
        except ZeroDivisionError:
            res.append(0)
            print("Division by zero")
        except (TypeError, ValueError):
            res.append(0)
            print("wrong type")
        finally:
            i += 1
        if len(my_list_1) != len(my_list_2) and out_range:
            print("Out of range")

    return res
