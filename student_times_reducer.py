#!/usr/bin/python

# key = author_id 
# value = hour of student activity in forum

import sys

old_key = None
student_hours = {}

def print_results(key, peak_hours):
    # finds the hours which has maximum values (the hours which this student has
    # the highest activities in forum)
    max = 0
    max_values = []
    for k,v in peak_hours.items():
	if max < v:
	    max = v
	    max_values = []
	    max_values.append(k)
	elif max == v:
	    max_values.append(k)
    
    # print out the results
    for i in range(0, len(max_values)):
	print key, "\t", max_values[i]

# loop around the data:
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # something has gone wrong. Skip this line.
        continue

    this_key, this_hour = data_mapped

    if old_key and old_key != this_key:
	print_results(old_key, student_hours)
        old_key = this_key;
	student_hours = {}

    old_key = this_key

    # add this_hour to the list of hours which student has activities in
    if this_hour not in student_hours:
	student_hours[this_hour] = 0

    # the number of the student activity in this_hour of day
    student_hours[this_hour] += 1	

if old_key != None:
    print_results(old_key, student_hours)
