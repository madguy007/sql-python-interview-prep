# insight.md

## Key Concept — Consecutive Event Detection

This problem is a classic example of a **Gaps and Islands problem**, which is common in analytics tasks such as:

* detecting user activity streaks
* login streak analysis
* trading activity sequences
* churn and retention analysis

The goal is to identify **continuous sequences of events**.

---

## Approach 1 — Sequence Grouping (Gaps and Islands)

Steps:

1. Assign a row number to each order per customer.

```
ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date)
```

2. Subtract the row number from the date.

```
order_date - rn * INTERVAL '1 day'
```

This normalizes consecutive dates into the **same group identifier**.

Example:

| order_date | rn | grp    |
| ---------- | -- | ------ |
| Jan 1      | 1  | Dec 31 |
| Jan 2      | 2  | Dec 31 |
| Jan 10     | 3  | Jan 7  |

Orders on **Jan1 and Jan2 share the same group**, meaning they are consecutive.

We then group by `(customer_id, grp)` and count sequence length.

---

## Approach 2 — LAG()

`LAG()` allows comparing the current row with the **previous row**.

```
LAG(order_date) OVER(PARTITION BY customer_id ORDER BY order_date)
```

Then we simply check:

```
order_date = previous_order_date + 1 day
```

This approach is usually the **expected interview answer**.

---

## Important SQL Insight — SELECT vs GROUP BY

Many developers misunderstand this rule.

### SQL Requirement

Every column in `SELECT` must be either:

* present in `GROUP BY`, or
* inside an aggregate function.

Example (invalid):

```
SELECT customer_id, order_date
FROM orders
GROUP BY customer_id;
```

`order_date` is neither grouped nor aggregated.

---

### Reverse Rule (Important)

A column in `GROUP BY` **does NOT have to appear in SELECT**.

Example:

```
SELECT customer_id
FROM orders
GROUP BY customer_id, order_date;
```

This is valid because `order_date` is used **only to form groups**, not to be displayed.

---

### Why We Used It Here

In the solution:

```
GROUP BY customer_id, grp
```

`grp` is used to **identify consecutive order sequences**, but we only need to **return the customer_id**, so `grp` does not need to appear in the final SELECT.

---

## Interview Takeaway

Understanding the difference between:

* **GROUP BY (row collapsing)**
* **Window functions (row preserving)**

is a key analytical SQL skill that interviewers frequently test.