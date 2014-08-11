#!/usr/bin/python

# key = id or parent_id (if the post is an answer or comment)
# value = author_id (student)
# output is the key/value tuple separated by tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) == 19:
	tagnames = line[2].split()
	if line[5] == "question":
	    print "%s\t%s" % (line[0], line[3])
	else:
	    print "%s\t%s" % (line[6], line[3])
