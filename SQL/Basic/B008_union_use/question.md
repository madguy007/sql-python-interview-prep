Employees With Missing Information

Write a solution to report the IDs of all the employees with missing information.

The information of an employee is considered missing if:
1. The employee's name is missing.
2. The employee's salary is missing.

You are given two tables:

Employees  
- employee_id  
- name  

Salaries  
- employee_id  
- salary  

Return the result table ordered by employee_id in ascending order.

Example:

Input:
Employees table
employee_id | name
2           | Crew
4           | Haven
5           | Kristian

Salaries table
employee_id | salary
1           | 22517
2           | 63539
4           | 63539

Output:
employee_id
1
2

Explanation:
Employee 1 has salary but no name.
Employee 2 has name but no salary.