#!/usr/bin/python3

import dis


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c

# print(magic_calculation(1, 2, 3))
# print(magic_calculation(2, 1, 3))
# print(magic_calculation(3, 1, 2))


dis.dis(magic_calculation)
