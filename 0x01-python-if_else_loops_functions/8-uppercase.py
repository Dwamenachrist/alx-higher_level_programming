#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a newline.""" 
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Detect lowercase
            upper_char = chr(ord(char) - 32)  # Convert to uppercase
            print(upper_char, end="")  
        else:
            print(char, end="")  # No conversion if already uppercase
    print()  # Add a newline at the end 
