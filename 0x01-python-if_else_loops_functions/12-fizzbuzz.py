#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers 1-100, replacing multiples of 3 with 'Fizz', 5 with 'Buzz', and 15 with 'FizzBuzz'."""   
    for num in range(1, 101):
        output = ""  # Start with an empty output string
        if num % 15 == 0: 
            output += "FizzBuzz" 
        elif num % 3 == 0:
            output += "Fizz"  
        elif num % 5 == 0:
            output += "Buzz"  
        else:
            output = str(num)  # Convert the number to a string
        print(output, end=" ") 
