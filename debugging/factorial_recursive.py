#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Recursive function to calculate the factorial of a number.

    Parameters:
    - n (int): The number whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
