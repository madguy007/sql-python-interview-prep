# Count Customers With More Than 5 Orders

## Problem
You are given an `orders` table containing information about customer orders.

### Table: orders

| Column | Type |
|------|------|
| order_id | INT |
| customer_id | INT |

## Task
Write a SQL query to **count how many customers have placed more than 5 orders**.

## Expected Output
A single number representing the **total number of customers** who placed more than 5 orders.

## Example

### Input

orders

| order_id | customer_id |
|----------|-------------|
| 1 | 101 |
| 2 | 101 |
| 3 | 101 |
| 4 | 101 |
| 5 | 101 |
| 6 | 101 |
| 7 | 102 |
| 8 | 102 |
| 9 | 103 |

### Explanation
Customer **101 placed 6 orders**, which is greater than 5.

### Output

| customer_count |
|----------------|
| 1 |