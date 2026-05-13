-- 1. Check for NULL values
SELECT *
FROM employees
WHERE manager_id IS NULL;


-- 2. Check for NOT NULL values
SELECT *
FROM employees
WHERE manager_id IS NOT NULL;


-- 3. Replace NULL values using COALESCE()
SELECT name,
       COALESCE(phone_number, 'Not Provided') AS contact
FROM customers;


-- 4. MySQL alternative using IFNULL()
SELECT name,
       IFNULL(phone_number, 'Not Provided') AS contact
FROM customers;


-- 5. NULL handling in aggregations
SELECT AVG(salary) AS avg_salary
FROM employees;


-- 6. Conditional NULL checks using CASE
SELECT name,
       CASE
           WHEN salary IS NULL THEN 'Unknown'
           ELSE 'Known'
       END AS salary_status
FROM employees;