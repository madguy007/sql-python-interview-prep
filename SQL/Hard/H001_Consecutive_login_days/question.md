# SQL Interview Question 3

## Problem
Find users who logged in for 3 or more consecutive days.

## Table Structure

Logins
---------
user_id (int)
login_date (date)

## Requirement
Return:
- user_id

Only those users who have logged in on at least 3 consecutive calendar days.

## Example

Input:

user_id | login_date
1       | 2024-01-10
1       | 2024-01-11
1       | 2024-01-13
1       | 2024-01-14
1       | 2024-01-15

Output:
1

Explanation:
Jan 13, Jan 14, Jan 15 are 3 consecutive days.
