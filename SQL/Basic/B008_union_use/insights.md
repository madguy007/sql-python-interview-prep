At first glance this problem looks tricky because we are dealing with two different tables and the requirement is to detect "missing information". But the key idea is to simplify the logic.

Instead of thinking about names and salaries directly, think about employee_id presence across the two tables.

An employee has complete information only if:
- Their employee_id exists in Employees
- AND their employee_id exists in Salaries

So missing information means the employee_id appears in only one table but not the other.

Step 1: Find employees who have salary but no name.
We check the Salaries table and see if the employee_id does NOT exist in Employees.

SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)

Step 2: Find employees who have name but no salary.
We check the Employees table and see if the employee_id does NOT exist in Salaries.

SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)

Step 3: Combine both results using UNION.

UNION merges both result sets and automatically removes duplicates.

Step 4: Sort the final result by employee_id using ORDER BY.

The important insight is that many problems that look complex can be reduced to simple set logic:
- "Present in A but not in B"
- "Present in B but not in A"

SQL operations like UNION, INTERSECT, and EXCEPT are powerful tools for solving such problems cleanly and efficiently.