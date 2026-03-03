# Google SQL Interview Question

## Problem

Find the percentage of employees in each department who earn more than the company-wide average salary.

## Table Structure

Employee(
    employee_id,
    salary,
    department_id
)

## Requirements

- Company-wide average means:
  
  SELECT AVG(salary) FROM Employee

- For each department:
  - Count employees with salary > company-wide average
  - Divide by total employees in that department
  - Multiply by 100
  - Round to 2 decimal places

## Output

Return:
- department_id
- percentage
