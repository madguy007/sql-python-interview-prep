# solution.sql

## Solution 1 — Sequence Grouping (Advanced “Gaps and Islands” Approach)

```sql
WITH cte1 AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER(
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS rn
    FROM orders
),
cte2 AS (
    SELECT 
        customer_id,
        order_date - rn * INTERVAL '1 day' AS grp
    FROM cte1
)

SELECT customer_id
FROM cte2
GROUP BY customer_id, grp
HAVING COUNT(*) >= 2;
```

---

## Solution 2 — Using LAG() (Simpler Interview Solution)

```sql
SELECT DISTINCT customer_id
FROM (
    SELECT 
        customer_id,
        order_date,
        LAG(order_date) OVER(
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS prev_date
    FROM orders
) t
WHERE order_date = prev_date + INTERVAL '1 day';
```