#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_list = []
    for elem in my_list:
        if elem % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
