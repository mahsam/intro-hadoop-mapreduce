#!/usr/bin/python

# key = author_id
# value = hour (from added_at field)
# assumption: ignore the offset for added_at field
# output is the key/value pair separated by tab

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    try:
	if len(line) == 19:
	    added_at = line[8]
	    added_at_datetime = added_at[:added_at.find('.')]
	    peak_hour = datetime.strptime(added_at_datetime, "%Y-%m-%d %H:%M:%S").hour
	    print "%s\t%s" % (line[3], peak_hour)
    except ValueError:
	pass
