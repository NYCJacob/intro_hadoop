#!/usr/bin/python

import sys

oldKey = None
hitsTotal = 0
# Loop around the data
#

for line in sys.stdin:
    thisKey = line
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitsTotal
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += 1


