#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    arguments = argv[1:]
    
    num_arguments = len(arguments)
    
    if num_arguments != 1:
        plural = 's'
    else:
        plural = ''
    
    message = "Number of argument{}: {}".format(plural, num_arguments)
    print(message, end='')

    if num_arguments > 0:
        print(":")
        index = 1
        for arg in arguments:
            print("{}: {}".format(index, arg))
            index += 1
    else:
        print(".")
