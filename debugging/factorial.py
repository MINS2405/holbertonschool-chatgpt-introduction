#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            input_number = int(sys.argv[1])
            if input_number < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(factorial(input_number))
        except ValueError:
            print("Please provide a valid integer as input.")
    else:
        print("Usage: ./factorial.py <number>")