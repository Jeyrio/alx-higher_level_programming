#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':

    arguments = argv[1:]
    arg_count = len(arguments)

    if arg_count == 0:
        print(f"{arg_count} arguments.")

    elif arg_count == 1:
        print(f"{arg_count} argument:")
        print(f"{arg_count}: {arguments[0]}")

    else:
        print(f"{arg_count} arguments:")

        for arg in range(0, arg_count):
            print(f"{arg + 1}: {arguments[arg]}")
