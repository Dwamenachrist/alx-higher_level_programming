#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character.

    Args:
        sentence: The input string.

    Returns:
        A tuple containing:
            * The length of the string.
            * The first character if the string is not empty, otherwise None.
    """

    string_length = len(sentence)
    first_char = sentence[0] if sentence else None

    return string_length, first_char
