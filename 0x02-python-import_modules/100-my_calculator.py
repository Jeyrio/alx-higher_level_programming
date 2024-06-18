#!/usr/bin/python3

if __name__ == "__main__":
    
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    arguments = argv[1:]

    num_argument = len(arguments)
    if num_argument != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(arguments[0])
    operator = arguments[1]
    b = int(arguments[2])

    operators = ["+", "-", "*", "/"]
    
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

    if operator != operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
