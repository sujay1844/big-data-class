#!/usr/bin/env python

import sys
from collections import defaultdict

# Create a default dictionary of integers to count nucleotide occurrences
nucleotide_counts = defaultdict(int)

# Read each line from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from the mapper
    position_nucleotide, count = line.split('\t', 1)

    # Convert the count to int and add it to the corresponding nucleotide occurrence
    count = int(count)
    nucleotide_counts[position_nucleotide] += count

# Output the total count for each position and nucleotide
for position_nucleotide, count in nucleotide_counts.items():
    print(f'{position_nucleotide}\t{count}')
