#!/usr/bin/env python
import colorama
from colorama import Fore, Style


def binomial(n):
    for i in range(n + 1):
        output = ""
        for j in range(i + 1):
            if j == 0:
                output += f"{Fore.LIGHTBLACK_EX}1{Style.RESET_ALL}"
            else:
                coef = str(i * (i - j + 1) // j)
                output += f" ({Fore.BLUE}{coef}{Style.RESET_ALL})"
        print(output)


if __name__ == '__main__':
    colorama.init()
    binomial(5)
