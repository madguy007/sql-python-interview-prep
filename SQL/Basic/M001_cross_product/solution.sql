-- Solution using explicit JOIN

SELECT c.cust_name,
       s.name,
       s.city
FROM customer c
JOIN salesman s
  ON s.city = c.city;
