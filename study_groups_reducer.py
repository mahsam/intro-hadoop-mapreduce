#!/usr/bin/python

# key = forum id
# value = author_id (student id) 

import sys

old_key = None
students_list = []

def print_results(key, students_list):
    # print out the results
    print "%s\t%s" % (key, students_list)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # something has gone wrong. Skip this line.
        continue

    this_key, this_student = data_mapped

    if old_key and old_key != this_key:
	print_results(old_key,students_list)
        old_key = this_key;
	students_list = []

    old_key = this_key

    # add the student to the list of forum students
    students_list.append(this_student)

if old_key != None:
    print_results(old_key,students_list)
