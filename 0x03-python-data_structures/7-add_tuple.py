#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples.

    Args:
        tuple_a: The first tuple.
        tuple_b: The second tuple.

    Returns:
        A new tuple containing the sum of the first two elements from 
        each input tuple.
    """

    # Handle shorter tuples by padding with zeros as needed
    tuple_a += (0, 0)  
    tuple_b += (0, 0) 

    # Calculate the sum for element 1 & 2, from 'padded' tuples 
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]) 
    return result
