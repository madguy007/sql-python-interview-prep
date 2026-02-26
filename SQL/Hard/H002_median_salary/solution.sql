-- Median salary using window functions

WITH cte AS (
    SELECT salary,
           ROW_NUMBER() OVER (ORDER BY salary) AS rn,
           COUNT(*) OVER () AS total_count
    FROM Employee
)

SELECT AVG(salary) AS median_salary
FROM cte
WHERE rn IN (
    FLOOR((total_count + 1) / 2.0),
    CEIL((total_count + 1) / 2.0)
);
