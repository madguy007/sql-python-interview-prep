# Insights

## 1. Core Objective

Find the most frequently ordered item for each customer.

---

## 2. Step 1: Count Orders

First, group data by:

- customer_id
- product_name

SELECT customer_id, product_name, COUNT(*) AS order_count
GROUP BY customer_id, product_name

This gives total orders per product per customer.

---

## 3. The Main Challenge

How do we retrieve the maximum order_count per customer
when multiple products have the same count?

Example:

Customer B ordered:
curry  -> 2
sushi  -> 2
ramen  -> 2

All three are maximum.

Using only:

MAX(order_count)

returns just the number 2,
but does not return all corresponding product rows.

---

## 4. Why Aggregate Functions Alone Fail

Aggregate functions (MAX, SUM, COUNT) collapse rows.

We need to:
- Preserve rows
- Rank them within each customer
- Filter the highest-ranked rows

---

## 5. Solution: Window Functions

DENSE_RANK() OVER (
    PARTITION BY customer_id
    ORDER BY order_count DESC
)

Why DENSE_RANK?

- Handles duplicates properly
- Does not skip rank values
- Returns all tied maximum rows when filtering WHERE rnk = 1

---

## 6. Key Concept Learned

Aggregate functions → Reduce rows  
Window functions → Preserve rows  

Window functions are essential when:
- You need ranking
- You need Top-N per group
- You need to handle ties correctly

---

## 7. Extension

To get Top 3 items per customer:

WHERE rnk <= 3

This makes the solution scalable and interview-ready.
