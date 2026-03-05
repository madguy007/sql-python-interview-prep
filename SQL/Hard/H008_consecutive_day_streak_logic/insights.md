# Insights: Detecting Increasing Activity Streaks

## 1️⃣ Step 1: Daily Aggregation

We first calculate how many actions each user performed per day.

SELECT user_id, activity_date, COUNT(*)

This produces one row per user per day with the total number of actions.

---

## 2️⃣ Step 2: Compare With Previous Day

Using LAG():

action_count > LAG(action_count)

This determines whether the activity increased compared to the previous day.

Example:

| date | actions | inc |
|------|--------|-----|
| Jan1 | 2 | NULL |
| Jan2 | 3 | 1 |
| Jan3 | 5 | 1 |
| Jan4 | 4 | 0 |
| Jan5 | 6 | 1 |

inc = 1 means the activity increased compared to the previous day.

---

## 3️⃣ Why We Filter With `WHERE inc = 1`

Only rows representing **increase events** are relevant for streak detection.

Example pattern:

↑ ↑ ↓ ↑ ↑

Filtering keeps:

↑ ↑   ↑ ↑

The decreases break streaks, so they are excluded.

---

## 4️⃣ Why Two ROW_NUMBER Functions Are Used

Two row numbers are computed:

ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date)

Counts every row sequentially.

ROW_NUMBER() OVER (PARTITION BY user_id, inc ORDER BY activity_date)

Resets whenever the value of `inc` changes.

---

## 5️⃣ Why `ROW_NUMBER - ROW_NUMBER` Works

We compute:

g = rn1 - rn2

Example:

| date | inc | rn1 | rn2 | g |
|------|-----|-----|-----|---|
| Jan2 | 1 | 2 | 1 | 1 |
| Jan3 | 1 | 3 | 2 | 1 |
| Jan4 | 0 | 4 | 1 | 3 |
| Jan5 | 1 | 5 | 3 | 2 |
| Jan6 | 1 | 6 | 4 | 2 |

Rows with the **same g value belong to the same streak**.

---

## 6️⃣ Detecting Streak Length

Each row with inc = 1 represents one increase.

For 3 consecutive increases:

Day1 → Day2 ↑  
Day2 → Day3 ↑  
Day3 → Day4 ↑  

This results in **3 increase rows**.

Therefore:

HAVING COUNT(*) >= 3

detects users with at least 3 consecutive increasing days.

---

## 7️⃣ Key SQL Pattern

The technique:

ROW_NUMBER() OVER (A)
-
ROW_NUMBER() OVER (A, condition)

is commonly used to detect **streaks or consecutive patterns** in SQL.

Applications include:

- login streak detection
- user engagement analysis
- price increase streaks
- retention metrics
- fraud detection patterns