#!/usr/bin/env python
import re

def binomial(n):
    for i in range(n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(' ', end='')
        # Print first number
        coef = '1'
        print(re.sub(r'(1)', r'\033[91m\1\033[0m', coef), end="")
        # Print rest of row
        for j in range(1, i+1):
            coef = str(i * (i-j+1) // j)
            print(' (' + re.sub(r'(\d)', r'\033[34m\1\033[0m', coef) + ')', end="")
        print()

if __name__ == '__main__':
    binomial(15)
