You are given a table named Department with the following columns:
- id (integer): Department ID
- month (varchar): Month name (Jan, Feb, Mar, ..., Dec)
- revenue (integer): Revenue generated in that month

Write a SQL query to transform (pivot) the data such that each row represents a department (id), and each month appears as a separate column showing the total revenue for that month.

If a department has no revenue for a particular month, return NULL for that month.

The output should have the following columns:
id, Jan_Revenue, Feb_Revenue, ..., Dec_Revenue