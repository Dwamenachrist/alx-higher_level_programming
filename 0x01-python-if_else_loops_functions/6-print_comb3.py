#!/usr/bin/python3
for i in range(10):    # Outer loop for the first digit
    for j in range(i + 1, 10):  # Inner loop for the second digit (starts higher)
        print("{}{}".format(i, j), end=", ")
print()