#!/usr/bin/env python

import sys

# Define a constant for the number of positions to consider
POSITIONS = 10

# Read each line from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Skip the identifier lines in the FASTA file
    if line.startswith('>'):
        continue

    # Process only the first POSITIONS characters of the line
    for i in range(min(POSITIONS, len(line))):
        # Output the position and nucleotide
        # Format: position_nucleotide   1
        print(f'{i+1}_{line[i]}\t1')
