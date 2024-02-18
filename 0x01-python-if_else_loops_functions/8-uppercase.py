#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a newline."""
    for char in str:
        print(chr(ord(char) - 32 if 97 <= ord(char) <= 122 else ord(char)), end="")
    print() 

