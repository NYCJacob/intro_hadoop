#!/usr/bin/python

#
# 6 field in web log is the webpage accessed
# need to strip off domain to merge same page different access path

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        print "{0}".format(data[6].replace("http://www.the-associates.co.uk","/"))
    else:
        continue
