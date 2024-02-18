#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) not in 'qe':  # Filter out 'q' and 'e' 
        print(chr(i),
              end="")
