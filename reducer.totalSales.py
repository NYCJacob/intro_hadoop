#!/usr/bin/python

import sys

salesTotalValue = 0.0
oldKey = None
counter = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# Total all sales amount and track total number of sales

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    counter += 1
    salesTotalValue += float(thisSale)

print counter, "\t", format(salesTotalValue, '.2f')
