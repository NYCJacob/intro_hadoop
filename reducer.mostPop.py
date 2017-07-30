#!/usr/bin/python

import sys

oldKey = None
hitsTotal = 0
topScore = 0
topPage = ""

# Loop around the data
#

for line in sys.stdin:
    thisKey = line

# key change mean end of key listing    
    if oldKey and oldKey != thisKey:

# check if hits greater than topScore
        if hitsTotal > topScore:
             topScore = hitsTotal
             topPage = thisKey       
# reset hitsTotal
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += 1

print topScore, "\t", topPage
