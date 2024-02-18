#!/usr/bin/python3
def print_last_digit(number):
    """Prints and returns the last digit of a given number."""
    last_digit = abs(number) % 10  # Extract last digit handling negatives
    print(last_digit, end="") 
    return last_digit 
