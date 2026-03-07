## Important Note

We cannot write:

SELECT COUNT(SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5)

because `COUNT()` expects a **column or expression**, not a **query**.

So we must first create a **subquery** and then count its rows.

Correct pattern:

SELECT COUNT(*)
FROM (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(order_id) > 5
) AS t;