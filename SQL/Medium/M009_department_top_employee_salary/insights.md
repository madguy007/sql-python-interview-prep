The goal is to find employees whose salary is the highest within their department.

Each employee record contains a DepartmentId which connects it to the Department table.  
The Department table provides the department name, so we join Employee and Department using Employee.DepartmentId = Department.Id.

The main challenge is identifying the maximum salary per department.

Approach 1 uses GROUP BY to compute the maximum salary for each department.  
This produces pairs like (DepartmentId, MaxSalary).  
The outer query then selects employees whose (DepartmentId, Salary) matches those pairs.

Approach 2 uses a window function.  
RANK() partitions employees by department and orders them by salary descending.  
The highest salary in each department receives rank 1.  
Filtering for rank = 1 returns the top earners.

Approach 3 uses a correlated subquery.  
For each employee row, SQL calculates the maximum salary in that employee's department and checks if the employee's salary matches it.

Approach 4 uses a self join.  
Each employee is compared with other employees in the same department who might have a higher salary.  
If no such employee exists (e2.Id IS NULL), then that employee must have the highest salary.

Key SQL concepts used:
- JOIN to combine Employee and Department tables
- GROUP BY and MAX() for aggregation
- Window functions like RANK() with PARTITION BY
- Correlated subqueries for row-by-row comparisons
- Self joins to compare rows within the same table