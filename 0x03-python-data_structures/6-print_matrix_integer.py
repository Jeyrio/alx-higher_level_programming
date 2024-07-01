#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_elements = []
        for element in row:
            formatted_elements.append("{:d}".format(element))
        print(" ".join(formatted_elements))
