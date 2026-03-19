You are given a table named Traffic with the following columns:
- user_id (integer)
- activity (varchar): can be 'login', 'logout', etc.
- activity_date (date)

There is no primary key and the table may contain duplicate rows.

Write a SQL query to report, for every date within at most 90 days from '2019-06-30', the number of users who logged in for the first time on that date.

Return the result with columns:
- login_date
- user_count