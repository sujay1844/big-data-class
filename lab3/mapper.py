#!/usr/bin/env python
import sys
import re

# Input comes from stdin
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Remove punctuation with regex
    line = re.sub(r'[^\w\s]','',line)
    
    # Split the line into words
    words = line.split()
    
    # Increase counters
    for word in words:
        # write the results to stdout;
        # what we output here will be the input for the Reducer step, i.e. the input for reducer.py
        # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (word, 1))
