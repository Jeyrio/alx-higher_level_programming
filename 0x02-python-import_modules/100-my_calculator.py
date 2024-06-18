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

    operators = {"+":add, "-":sub, "*":mul, "/":div}
    if operator not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))
