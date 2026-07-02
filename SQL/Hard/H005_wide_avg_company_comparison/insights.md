# Insights: Conditional Aggregation & Why SUM Is Used Instead of COUNT

## 1️⃣ Why Not Use COUNT(condition)?

Many developers try:

COUNT(salary > company_avg)

This does NOT work as expected.

Reason:
COUNT(expression) counts non-NULL values.
The boolean expression (salary > avg) evaluates to TRUE or FALSE,
but COUNT does not filter based on TRUE.
It simply counts non-null results.

So it will count all rows, not just matching rows.

---

## 2️⃣ Why SUM(CASE ...) Works

We use:

SUM(CASE WHEN salary > company_avg THEN 1 ELSE 0 END)

Explanation:

- When condition is TRUE → return 1
- When FALSE → return 0
- SUM adds the 1’s
- That effectively counts matching rows

Example:

| salary | > avg | CASE result |
|--------|-------|------------|
| 90000  | Yes   | 1          |
| 50000  | No    | 0          |
| 80000  | Yes   | 1          |

SUM = 1 + 0 + 1 = 2

That equals number of employees earning above average.

This is called **conditional aggregation**.

---

## 3️⃣ Why This Approach Is Cleaner

Using SUM(CASE...) inside GROUP BY:

- Avoids multiple CTE layers
- Avoids window functions
- Avoids extra joins
- Makes the logic readable and compact
- Scales well

The no-CTE approach:

SUM(CASE WHEN salary > (SELECT AVG(salary) FROM Employee) THEN 1 ELSE 0 END)

is concise and often preferred in interviews
because it demonstrates:

- Understanding of aggregation
- Understanding of boolean logic
- Ability to simplify queries

---

## 4️⃣ Key Concept

COUNT(*) → counts rows  
SUM(CASE...) → counts conditionally  

This pattern is widely used in:

- Conversion rate calculation
- Retention metrics
- Pass/fail ratios
- KPI percentage calculations

Understanding this distinction is critical for advanced SQL interviews.
