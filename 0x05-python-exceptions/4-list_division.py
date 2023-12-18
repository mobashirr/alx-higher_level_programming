#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Try to perform the division
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except (TypeError, ValueError):
            print("wrong type")
            division_result = 0
        except IndexError:
            print("out of range")
            break
        finally:
        # Add the result to the list, even if an exception occurred
            result.append(division_result)

    return result
