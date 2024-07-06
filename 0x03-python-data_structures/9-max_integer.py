#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list is None:
        return None
    max_value = my_list[0]
    for elem in my_list:
        if elem > max_value:
            max_value = elem
    return max_value
