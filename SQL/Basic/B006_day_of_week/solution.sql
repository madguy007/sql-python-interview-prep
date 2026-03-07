SELECT *
FROM employees
WHERE DAYOFWEEK(hire_date) IN (1,7);