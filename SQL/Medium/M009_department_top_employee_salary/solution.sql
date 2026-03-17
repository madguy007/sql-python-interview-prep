-- Approach 1: Using Tuple Comparison with Subquery
SELECT Department.Name AS Department, Employee.Name AS Employee, Salary
FROM Employee
JOIN Department
ON Employee.DepartmentId = Department.Id
WHERE (DepartmentId, Salary) IN (
        SELECT DepartmentId, MAX(Salary)
        FROM Employee
        GROUP BY DepartmentId
);

-- Approach 2: Using Window Function (Recommended)
SELECT Department, Employee, Salary
FROM (
        SELECT 
            d.Name AS Department,
            e.Name AS Employee,
            e.Salary,
            RANK() OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC) AS rnk
        FROM Employee e
        JOIN Department d
        ON e.DepartmentId = d.Id
) t
WHERE rnk = 1;

-- Approach 3: Using Correlated Subquery
SELECT d.Name AS Department, e.Name AS Employee, e.Salary
FROM Employee e
JOIN Department d
ON e.DepartmentId = d.Id
WHERE e.Salary = (
        SELECT MAX(Salary)
        FROM Employee
        WHERE DepartmentId = e.DepartmentId
);

-- Approach 4: Using Self Join
SELECT d.Name AS Department, e1.Name AS Employee, e1.Salary
FROM Employee e1
JOIN Department d
ON e1.DepartmentId = d.Id
LEFT JOIN Employee e2
ON e1.DepartmentId = e2.DepartmentId
AND e1.Salary < e2.Salary
WHERE e2.Id IS NULL;