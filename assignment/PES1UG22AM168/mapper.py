#!/usr/bin/env python

import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    tokens = line.split(",")
    
    # Parse input
    matrix_name = tokens[0]
    row = int(tokens[1])
    col = int(tokens[2])
    value = float(tokens[3])
    
    if matrix_name == 'a':
        for k in range(0, int(sys.argv[1])):
            print(f"{row},{k}\tA,{col},{value}")
    elif matrix_name == 'b':
        for i in range(0, int(sys.argv[2])):
            print(f"{i},{col}\tB,{row},{value}")
