SELECT 
EXTRACT(MONTH FROM order_date) AS month,
COUNT(order_id) AS order_count,
SUM(amount) AS monthly_revenue
FROM orders
GROUP BY EXTRACT(MONTH FROM order_date);