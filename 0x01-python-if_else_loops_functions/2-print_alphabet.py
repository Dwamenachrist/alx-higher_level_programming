#!/usr/bin/python3

"This code prints all lowercase letters of the English alphabet in sequence on a single line."
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")