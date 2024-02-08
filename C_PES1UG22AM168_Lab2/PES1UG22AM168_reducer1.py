#!/usr/bin/env python

import sys

current_motif = None
current_count = 0
motif = None

for line in sys.stdin:
    line = line.strip()

    # Parse the input we got from the mapper.py
    motif, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    count = int(count)

    if current_motif == motif:
        current_count += count
    else:
        if current_motif:
            print(f'{current_motif}\t{current_count}')
        current_count = count
        current_motif = motif

if current_motif == motif:
    print(f'{current_motif}\t{current_count}')
