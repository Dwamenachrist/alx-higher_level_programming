#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

# Check for correct number of arguments
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

# Extract values and operator
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

# Dictionary for operations
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

# Perform calculation or handle errors
if operator in operations:
    result = operations[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1) 
