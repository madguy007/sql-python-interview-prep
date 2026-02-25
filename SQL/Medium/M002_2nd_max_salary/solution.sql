-- Approach 1: Using MAX() (Most Portable & Interview-Friendly)

SELECT MAX(salary) AS second_highest_salary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);


-- Approach 2: Using DISTINCT + LIMIT/OFFSET (MySQL/PostgreSQL)

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS second_highest_salary;
