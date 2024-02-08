#!/usr/bin/env python

import sys

MOTIF = 'ATGTG'

for line in sys.stdin:
    line = line.strip()

    if not line or line.startswith('>'):
        continue

    for i in range(len(line) - len(MOTIF) + 1):
        window = line[i:i+len(MOTIF)]

        if window == MOTIF:
            print('%s\t%s' % (window, 1))
