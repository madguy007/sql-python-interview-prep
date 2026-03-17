Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+

Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

Write a SQL query to find employees who have the highest salary in each department.

Return the result with the department name, employee name, and salary.

The result table should contain:
Department | Employee | Salary

If multiple employees share the highest salary in the same department, include all of them.