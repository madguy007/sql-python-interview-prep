Table: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+

Primary Key:
(customer_id, visited_on)

Each row contains:
- customer_id -> unique customer ID
- name -> customer name
- visited_on -> date customer visited restaurant
- amount -> money spent by customer

Task:
Find 7-day moving sales analysis:
- Current day + previous 6 days
- Total revenue in window
- Average daily revenue
- Round average to 2 decimals
- Return ordered by visited_on
- Only include full 7-day windows