- This problem requires selecting:
  1. Employees with only one department
  2. Employees with multiple departments but only their primary one

Traditional Group By Difficulty:
- Using GROUP BY employee_id can give department counts
- But retrieving department_id conditionally becomes difficult
- You would need:
  - COUNT(*)
  - CASE statements
  - Additional joins/subqueries to recover department_id
- This creates more complexity and less readability

Example Group By thought process:
- GROUP BY employee_id
- If count = 1 → keep department_id
- If count > 1 → find row where primary_flag = 'Y'

Problem:
- GROUP BY collapses rows
- department_id detail is lost unless extra logic is added

Why Window Function is Better:
COUNT(*) OVER(PARTITION BY employee_id)

This:
- Counts departments per employee
- Preserves every original row
- No row collapsing
- Makes filtering straightforward

Logic:
- dept_count = 1 → employee has one department
- primary_flag = 'Y' → select designated primary department

Advantages:
- Cleaner logic
- No self join
- No aggregation loss
- Easier interview explanation

Key SQL Concepts:
- Window Functions
- PARTITION BY
- Conditional filtering
- Row preservation vs row aggregation

Interview Insight:
- GROUP BY is powerful for summarization
- Window functions are often superior when row-level detail must remain

This is a strong example of when window functions simplify otherwise messy grouped logic.