#!/usr/bin/python3

for char in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(chr(char), chr(char - 1 - 32)), end="") 
    #-1 print in reverse which is from y while 32 convert it to uppercase
