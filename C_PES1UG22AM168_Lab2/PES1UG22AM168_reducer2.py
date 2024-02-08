#!/usr/bin/env python

import sys

current_range = None
max_gc_content = 0

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input with the range as key and the gc content as value
    range, gc_content = line.split('\t', 1)
    gc_content = float(gc_content)

    # If this is the first iteration or if we've moved to a new range,
    # print the max gc content for the previous range and start over
    if current_range != range:
        if current_range is not None:
            print(f'{current_range}\t{max_gc_content}')
        current_range = range
        max_gc_content = gc_content
    else:
        # Update the max gc content if the current value is larger
        if gc_content > max_gc_content:
            max_gc_content = gc_content

# Don't forget to output the last range if needed!
if current_range == range:
    print(f'{current_range}\t{max_gc_content}')
