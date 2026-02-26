# SQL Interview Question 6

## Problem
For each customer, calculate the running total (cumulative sum) of order amounts ordered by order_date.

## Table Structure

Orders
---------
order_id (int)
customer_id (int)
order_date (date)
amount (int)

## Requirement

Return:
- customer_id
- order_date
- amount
- running_total

Rules:
- Running total must reset for each customer.
- Must be ordered by order_date.
- Use window functions (no correlated subqueries).
