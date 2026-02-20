-- Solution using INNER JOIN (recommended modern syntax)

SELECT o.ord_no,
       c.cust_name,
       o.customer_id,
       o.salesman_id
FROM orders o
JOIN customer c
  ON o.customer_id = c.customer_id
JOIN salesman s
  ON o.salesman_id = s.salesman_id
WHERE c.city <> s.city;
