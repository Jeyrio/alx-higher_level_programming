#!/usr/bin/python3

from sys import argv


def main():
    args = argv[1:]
    result = 0

    for arg in args:
        int_arg = int(arg)
        result += int_arg
    print(result)


if __name__ == '__main__':
    main()
