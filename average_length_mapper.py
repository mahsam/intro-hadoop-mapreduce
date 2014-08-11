#!/usr/bin/python

# key = id (forum_id)
# value = length of body
# assumption: ignore the comment posts
# output is the key/node_type(question or answer)/value tuple separated by tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) == 19:
	if line[5] == "question": # the forum_node_id is id
	    print "%s\t%s\t%s" % (line[0], "Q", len(line[4]))	
	elif line[5] == "answer": # the forum_node_id is parent_id
	    print "%s\t%s\t%s" % (line[7], "A", len(line[4]))
