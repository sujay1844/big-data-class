#!/usr/bin/env python

import sys

# Define constants
WINDOW_SIZE = 10

for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Skip the identifier lines in the FASTA file
    if line.startswith('>'):
        continue

    # Convert the sequence to upper case
    line = line.upper()

    # Use a sliding window to calculate GC content
    for i in range(len(line) - WINDOW_SIZE + 1):
        # Grab the current window
        window = line[i:i + WINDOW_SIZE]

        # Calculate GC content for the window
        gc_count = window.count('G') + window.count('C')
        gc_content = float(gc_count) / WINDOW_SIZE

        # Output the window position and gc content
        # Format: start_pos-end_pos\tgc_content
        print(f'{i+1}-{i + WINDOW_SIZE}\t{gc_content}')
