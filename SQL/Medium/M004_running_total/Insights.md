# Insights – Running Total & Window Frame Concept

## 1️⃣ Running Total Concept

A running total (cumulative sum) calculates the total from the beginning up to the current row.

In SQL, this is achieved using a window function:

SUM(amount) OVER (
    PARTITION BY customer_id
    ORDER BY order_date
)

- PARTITION BY resets calculation per customer.
- ORDER BY defines the sequence of accumulation.

Without ORDER BY:
The SUM() would return total per partition, not cumulative.

---

## 2️⃣ Window Function Execution Model

Window functions operate in this order:

1. Partition the data.
2. Order rows inside each partition.
3. Apply the window frame.
4. Compute the aggregate over the frame.

The "frame" defines which rows are visible to the current row.

---

## 3️⃣ Frame: ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

Meaning:
- Start from the first row in the partition.
- Include all rows up to the current row.

This produces a classic cumulative sum.


```

Example:

Date | Amount | Running Total
Jan1 | 100    | 100
Jan2 | 200    | 300
Jan3 | 150    | 450
```
Each row includes all previous rows.

---


## 4️⃣ Frame: ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING

ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING

Meaning:
- Start at current row.
- Include all rows after it.

This produces a reverse running total (suffix sum).
```
Example:

Date | Amount | Reverse Sum
Jan1 | 100    | 1000
Jan2 | 200    | 900
Jan3 | 300    | 700
Jan4 | 400    | 400
```
Each row includes itself and all future rows.

---

## 5️⃣ Why Frame Matters

Frame defines the visibility window for each row.

- UNBOUNDED PRECEDING → full history accumulation
- N PRECEDING → rolling window
- CURRENT ROW → single-row frame
- UNBOUNDED FOLLOWING → forward-looking accumulation

Understanding frame clauses is essential for advanced analytics queries, moving averages, and trend analysis.

---

## 6️⃣ Frame: ROWS BETWEEN 1 PRECEDING AND CURRENT ROW

ROWS BETWEEN 1 PRECEDING AND CURRENT ROW

Meaning:
- Include the current row.
- Include only the one row immediately before it.
- Exclude all other previous rows.

This creates a 2-row rolling window.
```
Example:

Date | Amount | Frame Rows Included | Result
Jan1 | 100    | [100]               | 100
Jan2 | 200    | [100, 200]          | 300
Jan3 | 300    | [200, 300]          | 500
Jan4 | 400    | [300, 400]          | 700
```
Notice:
- It does NOT include the full history.
- It only looks back 1 row.

This is called a rolling sum or moving window.

---

## 🔎 General Rule

ROWS BETWEEN N PRECEDING AND CURRENT ROW

Includes:
- Current row
- Previous N rows

Maximum rows included = N + 1

Examples:

- 1 PRECEDING → 2-row rolling window
- 2 PRECEDING → 3-row rolling window
- UNBOUNDED PRECEDING → cumulative sum

---

## Why This Is Useful

This pattern is used in:

- Moving averages
- Rolling revenue calculations
- Trend smoothing
- Time-series analytics

It is different from cumulative totals because it limits historical visibility.

##  Interview Concepts Tested

- Window functions
- Partitioning logic
- Order-sensitive aggregation
- Frame control
- Cumulative vs rolling vs reverse accumulation

Mastering frame clauses separates intermediate SQL users from advanced-level data professionals.
