# SQL Interview Question 2

## Problem
Find employees who earn more than their direct managers.

## Table Structure

Employee
---------
id (int)
name (varchar)
salary (int)
manager_id (int) -- references Employee.id

- manager_id is NULL for top-level managers.

## Requirement
Return:
- Employee id
- Employee name

Only those employees whose salary is strictly greater than their manager's salary.
