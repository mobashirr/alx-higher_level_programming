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
            out_range = True
        except ZeroDivisionError:
            print("Division by zero")
        except (TypeError, ValueError):
            res.append(0)
            print("Type error")
        finally:
            i += 1
            if len(my_list_1) > len(my_list_2) and out_range:
                print("Out of range")

    return res

# Example usage
my_list_1 = [10, 8, 4]
my_list_2 = [2, 4, 4]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)

print("--")

my_list_1 = [10, 8, 4, 4]
my_list_2 = [2, 0, "H", 2, 7]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)
