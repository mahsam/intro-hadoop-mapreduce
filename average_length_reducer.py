#!/usr/bin/python

# key = forum id
# type = question or answer
# value = the length of body

import sys

old_key = None
post_length = 0
answers_length = 0
answers_count = 0

def print_results(key, post_length, answers_length, answers_count):
    # print out the results
    print "%s\t%s\t%0.2f" % (key, post_length, 0 if answers_count == 0 else float(answers_length) / answers_count)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # something has gone wrong. Skip this line.
        continue

    this_key, this_type, this_length = data_mapped

    if old_key and old_key != this_key:
	print_results(old_key, post_length, answers_length, answers_count)
        old_key = this_key;
	post_length = 0
	answers_length = 0
	answers_count = 0

    old_key = this_key

    if this_type == "Q": # a question 
	post_length = this_length
    else: # an answer
	# get the sum of lengths and count the number to calculate the average
	answers_length += int(this_length)
	answers_count += 1 

if old_key != None:
    print_results(old_key, post_length, answers_length, answers_count)
