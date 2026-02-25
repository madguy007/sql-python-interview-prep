# Insights – Second Highest Salary

## Key Concepts Tested

1. Understanding DISTINCT
2. Handling duplicates correctly
3. Subqueries
4. Edge case handling (when second highest does not exist)
5. Aggregate functions on empty sets

---

## Why the MAX() Approach is Preferred

SELECT MAX(salary)
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

### Advantages:
- Database agnostic (works in MySQL, PostgreSQL, SQL Server, Oracle)
- Automatically returns NULL if no second highest exists
- Cleaner logic for whiteboard interviews
- No dependency on LIMIT / OFFSET

---

## Edge Case Behavior

If all salaries are:
100
100
100

Then:
WHERE salary < 100 → returns no rows

MAX() over empty set → NULL

This satisfies the problem requirement.

---

## Common Mistakes

- Using DISTINCT incorrectly (e.g., SELECT id, name, DISTINCT salary)
- Forgetting to remove duplicates
- Returning employee rows instead of just salary
- Not handling the NULL edge case
