#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    sorted_keys = sorted(a_dictionary.keys())  # Sort the keys

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))

# Example Usage
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
print_sorted_dictionary(a_dictionary)
