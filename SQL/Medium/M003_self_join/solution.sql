-- Employees earning more than their managers

SELECT e1.id,
       e1.name
FROM Employee e1
JOIN Employee e2
    ON e1.manager_id = e2.id
WHERE e1.salary > e2.salary;
