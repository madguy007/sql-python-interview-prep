-- Approach: Window Function (Best)

SELECT employee_id 
FROM (
    SELECT 
        employee_id,
        project_id,
        hours,
        AVG(hours) OVER (PARTITION BY project_id) AS avg_hrs
    FROM EmployeeProjects
) AS t
WHERE hours > avg_hrs
GROUP BY employee_id
HAVING COUNT(DISTINCT project_id) > 1;


-- Alternative: Using JOIN (without window function)

WITH avg_cte AS (
    SELECT 
        project_id,
        AVG(hours) AS avg_hrs
    FROM EmployeeProjects
    GROUP BY project_id
)

SELECT e.employee_id
FROM EmployeeProjects e
JOIN avg_cte a
  ON e.project_id = a.project_id
WHERE e.hours > a.avg_hrs
GROUP BY e.employee_id
HAVING COUNT(DISTINCT e.project_id) > 1;