#!/usr/bin/python3
import sys 

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):  
        try:
            # Attempt to format, assume it's an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError): 
            # Skip silently on exceptions (non-integers)
            pass
    print("")  # Print a newline
    return count
