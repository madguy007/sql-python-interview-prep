You are given two tables:

Table: Friends
- id (integer): Primary key
- name (varchar): Name of the friend
- activity (varchar): Activity the friend participates in

Table: Activities
- id (integer): Primary key
- name (varchar): Activity name

Each friend participates in exactly one activity.

Write a SQL query to find the names of all activities that have neither the maximum nor the minimum number of participants.

Return the activity names.