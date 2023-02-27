#!/usr/bin/env python
import colorama
from colorama import Fore, Style


def binomial(n):
    for i in range(n + 1):
        output = ""
        for j in range(i + 1):
            if j == 0:
                output += '%s1%s' % (Fore.LIGHTBLACK_EX, Style.RESET_ALL)
            else:
                coef = str(i * (i - j + 1) // j)
                output += ' (%s%s%s)' % (Fore.BLUE, coef, Style.RESET_ALL)
        print(output)


if __name__ == '__main__':
    colorama.init()
    binomial(5)
