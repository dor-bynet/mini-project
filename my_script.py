#!/usr/bin/env python
import re

def binomial(n):
    for i in range(n+1):
        print('1', end="")
        for j in range(1, i+1):
            coef = str(i * (i-j+1) // j)
            print(' (' + re.sub(r'(\d)', r'\033[34m\1\033[0m', coef) + ')', end="")
        print()

if __name__ == '__main__':
    binomial(15)
