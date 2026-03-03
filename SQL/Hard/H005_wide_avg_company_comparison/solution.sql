-- ===============================
-- Approach 1: Using CTE
-- ===============================

WITH company_avg AS (
    SELECT AVG(salary) AS avg_salary
    FROM Employee
)
SELECT e.department_id,
       ROUND(
           100.0 *
           SUM(CASE 
                   WHEN e.salary > c.avg_salary THEN 1 
                   ELSE 0 
               END
           ) / COUNT(*),
       2) AS percentage
FROM Employee e
CROSS JOIN company_avg c
GROUP BY e.department_id;



-- ===============================
-- Approach 2: Without CTE (Inline Subquery)
-- ===============================

SELECT department_id,
       ROUND(
           100.0 *
           SUM(
               CASE 
                   WHEN salary > (SELECT AVG(salary) FROM Employee)
                   THEN 1
                   ELSE 0
               END
           ) / COUNT(*),
       2) AS percentage
FROM Employee
GROUP BY department_id;
