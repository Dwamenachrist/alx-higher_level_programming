#!/usr/bin/python3
import sys

# Access command-line arguments using the sys module
argv = sys.argv

# Calculate the number of arguments
num_args = len(argv) - 1  # Subtract 1 to exclude the script name itself

# Construct the output strings
if num_args == 0:
    print("{} arguments.".format(num_args))
elif num_args == 1:
    print("{} argument:".format(num_args))
else:
    print("{} arguments:".format(num_args))

# Print each argument and its position
for i in range(1, num_args + 1):
    print("{}: {}".format(i, argv[i])) 
