#!/usr/bin/python3
def number_keys(a_dictionary):

    return len(a_dictionary)  # Using the built-in len() function

# Example Usage
a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
