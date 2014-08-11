#!/usr/bin/python

# key = tagname
# value = will be the count of tagname in reducer
# output is the key/node_type(question or answer/comment) tuple separated by tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) == 19:
	tagnames = line[2].strip().split()
	if line[5] == "question":
	    for i in range(0, len(tagnames)):
		print "%s\t%s" % (tagnames[i].lower(), "Q")
	else:
	    for i in range(0, len(tagnames)):
		print "%s\t%s" % (tagnames[i].lower(), "A")
