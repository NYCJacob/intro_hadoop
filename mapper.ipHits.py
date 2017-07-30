#!/usr/bin/python

# mapper script to output ip as key from web log file

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        print "{0}".format(data[0])
    else:
        continue
