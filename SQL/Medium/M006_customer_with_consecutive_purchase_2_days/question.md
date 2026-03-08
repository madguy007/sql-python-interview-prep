# question.md

## Problem 24 — Customers With Consecutive Purchases (2 Days)

### Table

**orders**

| column      | type |
| ----------- | ---- |
| customer_id | INT  |
| order_date  | DATE |

### Example Data

| customer_id | order_date |
| ----------- | ---------- |
| 101         | 2023-01-01 |
| 101         | 2023-01-02 |
| 101         | 2023-01-10 |
| 102         | 2023-02-01 |
| 102         | 2023-02-03 |
| 103         | 2023-03-05 |
| 103         | 2023-03-06 |

### Task

Find **customers who placed orders on two or more consecutive days**.

A purchase is considered **consecutive** if the difference between two order dates is **exactly 1 day**.

### Expected Output

| customer_id |
| ----------- |
| 101         |
| 103         |

### Explanation

Customer **101**

```
2023-01-01
2023-01-02  ← consecutive
```

Customer **103**

```
2023-03-05
2023-03-06  ← consecutive
```

Customer **102**

```
2023-02-01
2023-02-03  ← gap of 2 days
```

So customer **102** is not included.