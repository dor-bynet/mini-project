#!/usr/bin/env python
import sys

# Set the text color to red
sys.stdout.write("\x1b[31m")

# Print the 1 digits
for i in range(1, 11):
    for j in range(1, i+1):
        if (j == 1 or j == i):
            # Set the text color to red
            sys.stdout.write("\x1b[31m")
            print(j, end=" ")
        else:
            # Set the text color to blue
            sys.stdout.write("\x1b[34m")
            print(j, end=" ")
    print()

# Set the text color to default
sys.stdout.write("\x1b[0m")
