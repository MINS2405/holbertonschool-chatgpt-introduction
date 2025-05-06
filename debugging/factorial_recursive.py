#!/usr/bin/python3
import sys

def factorial(n):
"""
Calculates the factorial of a given non-negative integer using recursion.

A factorial of a number `n` is the product of all positive integers less than or equal to `n`.
It is defined as:
- factorial(0) = 1
- factorial(n) = n * factorial(n-1) for n > 0

Parameters:
n (int): A non-negative integer for which the factorial is to be calculated.

Returns:
int: The factorial of the input number `n`.
"""
if n == 0:
return 1
else:
return n * factorial(n - 1)

# Get the input number from the command-line argument and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)