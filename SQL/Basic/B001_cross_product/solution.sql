-- Solution using explicit JOIN

SELECT c.cust_name,
       s.name,
       s.city
FROM customer c
CROSS JOIN salesman s
WHERE s.city = c.city;
