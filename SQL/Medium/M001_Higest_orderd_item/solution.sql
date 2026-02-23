-- Most Popular Item Per Customer

WITH order_counts AS (
    SELECT 
        s.customer_id,
        m.product_name,
        COUNT(*) AS order_count
    FROM sales s
    JOIN menu m
        ON s.product_id = m.product_id
    GROUP BY s.customer_id, m.product_name
)

SELECT customer_id, product_name, order_count
FROM (
    SELECT *,
           DENSE_RANK() OVER (
               PARTITION BY customer_id
               ORDER BY order_count DESC
           ) AS rnk
    FROM order_counts
) ranked
WHERE rnk = 1
ORDER BY customer_id;
