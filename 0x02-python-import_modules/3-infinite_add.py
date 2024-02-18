#!/usr/bin/python3
import sys

# Access command line arguments 
argv = sys.argv

# Initialize the sum
total = 0

# Calculate the sum
for i in range(1, len(argv)):  # Start from 1 to skip the script name
    total += int(argv[i])

# Print the result 
print(total)
