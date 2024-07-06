#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    for elem in my_list:
        if elem > max_value:
            max_value = elem
    return max_value
