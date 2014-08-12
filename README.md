Hadoop/MapReduce
======================

Here's some mapreduce programs that I wrote for the [Intro to Hadoop and MapReduce](https://www.udacity.com/course/ud617) course on Udacity.

You can download the dataset from [here](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz).

## MapReduce programs

**student_times_mapper.py & student_times_reducer.py**
- Finds for each student what is the hour during which the student has posted the most posts.

**average_length_mapper.py & average_length_reducer.py**
- Processes the forum_node data and returns the leghth of the post and the average answer (just answer, not comment) length for each post.

**popular_tags_mapper.py & popular_tags_reducer.py**
- Returns top 10 tags, ordered by the number of questions they appear in.

**study_groups_mapper.py & study_groups_reducer.py**
- For each forum thread (that is a question node with all it's answers and comments) returns a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
