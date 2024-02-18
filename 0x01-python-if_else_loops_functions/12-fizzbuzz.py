#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers 1-100, replacing multiples of 3 with 'Fizz', 5 with 'Buzz', and 15 with 'FizzBuzz'."""
    for num in range(1, 101):
        if num % 15 == 0:  # Check for FizzBuzz (multiples of BOTH 3 and 5)
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:  # Check for Fizz
            print("Fizz", end=" ")
        elif num % 5 == 0:  # Check for Buzz
            print("Buzz", end=" ")
        else:
            print(num, end=" ")  # Just print the number
