# Insights: Daily Aggregation + LAG + Ordering Logic

## 1️⃣ Why We First Use GROUP BY

We must first calculate daily transaction counts.

If we directly applied LAG() on raw Transactions table,
we would compare individual transaction rows,
not daily totals.

Correct logic:

SELECT user_id, transaction_date, COUNT(*)
GROUP BY user_id, transaction_date

Now each row represents one calendar day per user.

---

## 2️⃣ Why ORDER BY Inside CTE1 Is Not Needed

GROUP BY does NOT guarantee row order.

Even if we write:

GROUP BY user_id, transaction_date
ORDER BY transaction_date

That order is NOT guaranteed to persist into the next CTE.

SQL tables and CTEs are unordered sets.
The engine may rearrange rows during execution.

Therefore, relying on implicit ordering is unsafe.

---

## 3️⃣ Why ORDER BY Is Required Inside LAG()

Window functions require explicit ordering to define "previous".

LAG(curr_t) OVER (
    PARTITION BY user_id
    ORDER BY transaction_date
)

This tells SQL:

- Partition data by user
- Within each user, process rows in chronological order
- For each row, return previous day's transaction count

Without ORDER BY inside the window function,
the database is free to choose any row as "previous",
leading to nondeterministic results.

---

## 4️⃣ Important SQL Principle

Table ≠ Sorted  
CTE ≠ Sorted  
GROUP BY ≠ Sorted  

Only these guarantee order:

- ORDER BY in final SELECT
- ORDER BY inside window functions

If ORDER BY is missing inside LAG/LEAD,
the query is logically incomplete.

---

## 5️⃣ Final Logic Summary

Step 1 → Aggregate transactions per day  
Step 2 → Use LAG() with ORDER BY transaction_date  
Step 3 → Compare curr_t > prev_t  
Step 4 → Return distinct qualifying users  

This pattern is commonly tested in Uber and other product-company interviews.
