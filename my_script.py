#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def newton_binomial(n):
    coeffs = np.zeros((n+1, n+1))
    coeffs[0][0] = 1

    for i in range(1, n+1):
        coeffs[i][0] = 1
        for j in range(1, i+1):
            coeffs[i][j] = coeffs[i-1][j-1] + coeffs[i-1][j]

    max_coeff = np.max(coeffs)
    num_digits = len(str(max_coeff))

    for i in range(n+1):
        row_str = ""
        for j in range(i+1):
            coeff_str = str(int(coeffs[i][j])).rjust(num_digits)
            row_str += coeff_str + " "
        padding = " " * ((n-i) * (num_digits+1) // 2)
        print(padding + row_str)

    plt.imshow(coeffs, cmap='Blues', interpolation='nearest')
    plt.title(f"Newton binomial coefficients for n={n}")
    plt.show()

newton_binomial(15)
