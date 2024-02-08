#!/usr/bin/env python

import sys

# Initialize variables
current_key = None
current_row = None
current_col = None
current_value = 0.0

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Split the line into key and value
    key, value = line.split("\t")
    row, col = map(int, key.split(","))
    matrix, idx, val = value.split(",")
    idx = int(idx)
    val = float(val)
    
    # If we're still processing the same key...
    if key == current_key:
        if matrix == 'A':
            current_value += val * matrix_b_values[idx]
        else:
            current_value += val * matrix_a_values[idx]
    else:
        # If it's a new key and not the first input...
        if current_key:
            print(f"({current_row},{current_col})\t{current_value}")
        
        current_key = key
        current_row = row
        current_col = col
        current_value = 0.0
        
        # Initialize matrix A and B values
        matrix_a_values = [0.0] * int(sys.argv[1])
        matrix_b_values = [0.0] * int(sys.argv[2])
        
    # Store the values of matrix A and B
    if matrix == 'A':
        matrix_a_values[idx] = val
    else:
        matrix_b_values[idx] = val

# Output the last key-value pair if needed
if current_key:
    print(f"({current_row},{current_col})\t{current_value}")
