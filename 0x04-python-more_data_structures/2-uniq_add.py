#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_numbers = set(my_list)  # Convert to a set to remove duplicates
    return sum(unique_numbers)      # Efficiently sum the set elements

# Example usage
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result)) 
