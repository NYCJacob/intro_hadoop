#!/usr/bin/python

import sys

postsTotal = 0
oldAuthor = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    id, author, timePosted = data_mapped
    postTime = timePosted.split(" ")
    postTimeDetails = postTime[1].split(":")
    postHour = postTimeDetails[0]

    if oldAuthor and oldAuthor != author:
    # find hour time of most posts for this author


        print oldAuthor, "\t", postsTotal, "\t", postTimeDetails
        oldAuthor = author;
        postsTotal = 0

    oldAuthor = author
    postsTotal += 1

if oldAuthor != None:
    print oldAuthor, "\t", postsTotal

