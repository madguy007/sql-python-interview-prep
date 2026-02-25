# Insights – Employee vs Manager Salary

## Core Concept: Self Join

This problem tests understanding of self joins.

Since manager information exists in the same table,
we must join the Employee table to itself.

---

## Why e1 is Employee and e2 is Manager

Join condition:

e1.manager_id = e2.id

Explanation:

- manager_id exists in the employee row.
- It stores the id of that employee’s manager.
- Therefore:

e1 → employee  
e2 → manager  

Logical interpretation:

Employee (e1)  ──manager_id──▶  Manager (e2)

---

## Mental Model for Self Joins

Always identify:

1. Which column holds the foreign key?
2. That table alias represents the dependent entity.
3. The referenced id represents the parent entity.

Here:
- manager_id is the foreign key.
- So the table alias containing manager_id is the employee.

---

## Common Mistakes

- Writing "SELF JOIN" (invalid syntax).
- Reversing join logic and comparing salaries incorrectly.
- Forgetting that NULL values do not join.
- Returning all columns instead of required columns.

---

## Edge Case

Top-level managers (manager_id IS NULL)
do not appear in the result because:

NULL never equals any value in JOIN conditions.
