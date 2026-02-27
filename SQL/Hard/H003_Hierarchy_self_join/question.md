# Employees Reporting Hierarchy (Self Join) - Indirect relationship of manager up to three level.
```
Table: **Employees**

| employee_id | employee_name | manager_id |
|-------------|--------------|-----------|
| 1 | Boss | 1 |
| 3 | Alice | 3 |
| 2 | Bob | 1 |
| 4 | Daniel | 2 |
| 7 | Luis | 4 |
| 8 | John | 3 |
| 9 | Angela | 8 |
```
Write an SQL query to find the **employees whose manager's manager ultimately reports to employee 1**, but **exclude employee 1 itself**.

Use self joins to navigate the hierarchy.

Expected concept:

```
employee → manager → manager's manager
   e1         e2           e3
```

Conditions:

- `e3.manager_id = 1`
- `e1.employee_id != 1`

Return the employee IDs that satisfy the condition.

---
