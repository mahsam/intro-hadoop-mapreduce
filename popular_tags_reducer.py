#!/usr/bin/python

# key = tagname
# type = question or answer/comment
# topten_tuples and print_results are helper functions

import sys
import timeit

old_key = None
questions_count = 0
tag_counts = 0
topten_tags = []
topten_questions = []

def print_results(tuples_list):
    # print out the results
    for k in tuples_list:
	print "%s\t%s" % (k[0], k[1])

def topten_tuples(tuples_list, tagname, count):
    # calculate the top ten tagnames in a list of (tagname, count) tuples
    # tuples_list could be either questions or posts
    tuples_list.append((tagname, count))
    tuples_list = sorted(tuples_list, key=lambda k:k[1], reverse=True)
    if len(tuples_list) > 10:
	del tuples_list[10]

    return tuples_list

start_time = timeit.default_timer()
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # something has gone wrong. Skip this line.
        continue

    this_key, this_type = data_mapped

    if old_key and old_key != this_key:
	topten_tags = topten_tuples(topten_tags, old_key, tag_counts)
	topten_questions = topten_tuples(topten_questions, old_key, questions_count)
        old_key = this_key;
	questions_count = 0
	tag_counts = 0

    old_key = this_key

    if this_type == "Q": # a question
	# count the number of quesions which tagname appeared in
	questions_count += 1

    tag_counts += 1

if old_key != None:
    topten_tags = topten_tuples(topten_tags, old_key, tag_counts)
    topten_questions = topten_tuples(topten_questions, old_key, questions_count)

print "-----Posts-----"
print_results(topten_tags)
print "-----Questions-----"
print_results(topten_questions)
