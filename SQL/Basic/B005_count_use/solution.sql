SELECT COUNT(*) AS customer_count
FROM (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(order_id) > 5
) AS t;