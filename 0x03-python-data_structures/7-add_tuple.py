#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    result_1 = a1 + b1
    result_2 = a2 + b2

    total_result = (result_1, result_2)
    return total_result
