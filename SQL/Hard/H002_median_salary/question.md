# SQL Interview Question 8

## Problem
Find the median salary from the Employee table.

## Table Structure

Employee
---------
id (int)
name (varchar)
salary (int)

## Requirement

Return:
- median_salary

Rules:
- If total number of rows is odd → return the middle salary.
- If total number is even → return the average of the two middle salaries.
- Salaries must be considered in ascending order.
- Must work dynamically (no hardcoded row numbers).

## Example 1 (Odd)

Salaries:
10
20
30
40
50

Median = 30

## Example 2 (Even)

Salaries:
10
20
30
40

Median = (20 + 30) / 2 = 25
