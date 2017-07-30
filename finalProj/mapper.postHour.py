#!/usr/bin/python

# Format of each line is:
# there are 19 fields per line tab delineated
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")

    # check if 19 fields in stdin and not header row
    if len(data) == 19 and data[0] != 'id':
        authorId = data[3]
        postTime = data[8]

        #  spec states to ignore GMT offset so strip last three chars
        # .hour returns hour from datatime object formatted according to spec
        postHour = datetime.strptime(postTime[:-3], "%Y-%m-%d %H:%M:%S.%f").hour

        print "{0}\t{1}".format(authorId,postHour)

    # bad data skip
    else:
        continue


