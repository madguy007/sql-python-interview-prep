# Insights: Consecutive Days + Aggregation Logic

## 1️⃣ Why We First Use GROUP BY (Daily Aggregation)

A user can make multiple transactions on the same day.

Example:

| user_id | date       | amount |
|----------|------------|--------|
| 1        | Jan 1      | 400    |
| 1        | Jan 1      | 300    |
| 1        | Jan 2      | 200    |

If we directly apply ROW_NUMBER(), the same day will appear multiple times,
which breaks the consecutive-day logic.

So we must first aggregate per day:

SELECT user_id, transaction_date, SUM(amount)
GROUP BY user_id, transaction_date

Now each row represents one calendar day.

This ensures:
- Correct streak detection
- Correct total sum calculation

---

## 2️⃣ Why NOT Use DISTINCT Instead?

We might think of using:

SELECT DISTINCT user_id, transaction_date, amount

This is incorrect because:

- DISTINCT removes duplicate rows.
- It does NOT sum amounts.
- If a user has multiple transactions on the same day,
  DISTINCT would keep only one row and discard others.
- That causes loss of transaction amounts.

Example:

| user_id | date  | amount |
|----------|-------|--------|
| 1        | Jan 1 | 400    |
| 1        | Jan 1 | 300    |

DISTINCT keeps only one row.
Total becomes 400 (or 300) instead of 700.
That is incorrect.

GROUP BY preserves business logic.
DISTINCT may cause data loss.

---

## 3️⃣ Why "date - row_number" Works

For consecutive dates:

Jan 1 → rn = 1  
Jan 2 → rn = 2  
Jan 3 → rn = 3  

If we compute:

date - rn days

All values become the same constant.

That constant becomes the grouping key.

When a gap appears, the constant changes,
which naturally separates streaks.

This is known as the "Gaps and Islands" technique.

---

## 4️⃣ Final Logic Summary

Step 1 → Aggregate per day  
Step 2 → Assign row numbers per user  
Step 3 → Create streak group key  
Step 4 → Filter streaks:
    COUNT(*) >= 3
    AND SUM(daily_amount) > 1000

This pattern is commonly tested in advanced SQL interviews
at companies like Stripe, Amazon, and Airbnb.
