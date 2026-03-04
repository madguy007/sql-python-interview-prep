# Insights: Detecting Consecutive Increase Streaks

## 1️⃣ Step 1: Detect Price Increases

We first compare each price with the previous update using LAG.

Example:

| date | price | inc |
|------|------|------|
| Jan1 | 10 | NULL |
| Jan2 | 12 | 1 |
| Jan3 | 15 | 1 |
| Jan4 | 13 | 0 |
| Jan5 | 16 | 1 |
| Jan6 | 18 | 1 |

inc = 1 means the price increased compared to the previous update.

---

## 2️⃣ Why Two ROW_NUMBER Functions Are Used

Two row numbers are created:

ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY update_date)

Counts all rows sequentially.

ROW_NUMBER() OVER (PARTITION BY product_id, inc ORDER BY update_date)

Resets counting whenever the value of inc changes.

---

## 3️⃣ Why Subtracting Row Numbers Works

We compute:

g = rn1 - rn2

Example:

| date | inc | rn1 | rn2 | g |
|------|------|-----|-----|---|
| Jan2 | 1 | 2 | 1 | 1 |
| Jan3 | 1 | 3 | 2 | 1 |
| Jan4 | 0 | 4 | 1 | 3 |
| Jan5 | 1 | 5 | 3 | 2 |
| Jan6 | 1 | 6 | 4 | 2 |

Rows with the **same g value belong to the same streak**.

Example streaks:

Jan2–Jan3 → g = 1  
Jan5–Jan6 → g = 2

---

## 4️⃣ Detecting Streak Length

Each increase represents:

previous_price → current_price

So for 3 increasing prices we get:

price1 → price2 → price3 → price4

This produces **3 increases**.

The minimum valid pattern:

price1 → price2 → price3

This produces **2 increases**.

Therefore:

HAVING COUNT(*) >= 2

detects products with at least 3 consecutive increasing prices.

---

## 5️⃣ Key Pattern

The technique:

ROW_NUMBER() OVER (A)
-
ROW_NUMBER() OVER (A, condition)

is commonly used to detect **streaks** or **consecutive sequences** in SQL.

Applications include:

- login streak detection
- transaction streak analysis
- retention tracking
- anomaly detection
- fraud pattern analysis
