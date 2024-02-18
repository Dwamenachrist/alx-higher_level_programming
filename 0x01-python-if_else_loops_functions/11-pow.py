#!/usr/bin/python3
def pow(a, b):
    """Calculates the result of a raised to the power of b."""
    result = 1
    if b < 0:
        b = -b
        a = 1 / a
    for _ in range(b):
        result *= a
    return result

# Test cases
print(pow(2, 2))  # Output: 4
print(pow(98, 2))  # Output: 9604
print(pow(98, 0))  # Output: 1
print("{:.2f}".format(pow(100, -2)))  # Output: 0.01
print(pow(-4, 5))  # Output: -1024
