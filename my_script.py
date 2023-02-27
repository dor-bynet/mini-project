#!/usr/bin/env python
def newton_binomial(n): 
    for i in range(0, n): 
        for j in range(0, n-i-1): 
            print("   ", end=" ") 
        for j in range(0, i+1): 
            if(j == 0 or i == j): 
                print("\033[91m" + str(1) + "\033[0m", end="   ") 
            else: 
                print("\033[94m" + str(int(binomialCoeff(i, j))) + "\033[0m", end="   ")
        print("") 
  
def binomialCoeff(n, k): 
    res = 1
    if (k > n - k): 
        k = n - k 
    for i in range(0 , k): 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 
newton_binomial(10)
