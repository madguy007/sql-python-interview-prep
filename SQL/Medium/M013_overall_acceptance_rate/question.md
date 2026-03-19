You are given two tables:

Table: friend_request
- sender_id (integer)
- send_to_id (integer)
- request_date (date)

Table: request_accepted
- requester_id (integer)
- accepter_id (integer)
- accept_date (date)

Write a SQL query to find the overall acceptance rate of friend requests, defined as:

acceptance_rate = (number of accepted requests) / (number of total requests)

Return the result rounded to 2 decimal places.

Note:
- Duplicate records may exist.
- Acceptance should be counted based on unique (sender_id, send_to_id) pairs.