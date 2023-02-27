#!/usr/bin/env python
import re

def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

def color_digits(number):
    colored_number = ""
    for digit in str(number):
        if digit == "1":
            colored_number += "  \033[37m  " + digit + "  \033[0m  "
        else:
            colored_number += "  \033[34m  " + digit + "  \033[0m  "
    return colored_number

def print_binomial_theorem(n):
    for k in range(n+1):
        coefficient = binomial(n, k)
        colored_coefficient = color_digits(coefficient)
        print(colored_coefficient)

print_binomial_theorem(30)
