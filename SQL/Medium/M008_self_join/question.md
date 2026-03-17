Managers with Direct Reports

Table: Employee

+----+-------+-----------+
| id | name  | managerId |
+----+-------+-----------+
| 1  | John  | NULL      |
| 2  | Alice | 1         |
| 3  | Bob   | 1         |
| 4  | Mike  | 2         |
+----+-------+-----------+

Write a SQL query to find each manager and the number of employees who directly report to them.

Return the result with two columns:
- manager name
- number of direct reports