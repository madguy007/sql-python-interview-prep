# Most Popular Item Per Customer

## Problem Statement

Given three tables:

Table 1: sales  
Table 2: members  
Table 3: menu  

Write a query to determine which item was the most popular for each customer.

The result should return:

- customer_id
- product_name
- order_count

If multiple items have the same highest order count for a customer,
return all of them.

---

## Expected Output Format

customer_id | product_name | order_count
------------|--------------|------------
A           | ramen        | 3
B           | curry        | 2
B           | sushi        | 2
B           | ramen        | 2
C           | ramen        | 3

---

## Requirements

- Join appropriate tables
- Count orders per customer per product
- Handle ties correctly
- Use window functions for ranking
