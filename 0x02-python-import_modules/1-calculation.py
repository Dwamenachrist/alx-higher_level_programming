#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

# Define variables
a = 10
b = 5

# Perform calculations and print results
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b))) 
