#!/usr/bin/python3
def pow(a, b):
    """Calculates the result of a raised to the power of b."""
    result = 1  
    if b < 0:  # Handling negative exponents
        b = -b  
        a = 1 / a  
    for _ in range(b):  # _ is a placeholder since we only care about iterations
        result *= a 
    return result
