# Insights: Ranking Within Groups

## 1️⃣ Step 1: Aggregation

First we calculate the number of actions each user performed per day.

SELECT user_id, activity_date, COUNT(*)

This produces one row per user per day with their action count.

---

## 2️⃣ Why Ranking Is Required

The question asks for:

Top 2 users **per day**

This means ranking must be done separately for each date.

We achieve this using:

PARTITION BY activity_date

inside the window function.

---

## 3️⃣ Why DENSE_RANK Is Used

The problem states that ties should be included.

Example:

| user | actions |
|------|--------|
| A | 10 |
| B | 10 |
| C | 9 |

Using DENSE_RANK():

| user | rank |
|------|------|
| A | 1 |
| B | 1 |
| C | 2 |

All three users qualify when filtering with:

WHERE rank <= 2

If we used ROW_NUMBER(), ties would be broken arbitrarily and some users would be excluded.

---

## 4️⃣ Key SQL Pattern

This problem demonstrates a very common interview pattern:

1. Aggregate data
2. Rank within groups
3. Filter top N per group

General template:

SELECT *
FROM (
    SELECT ...,
           RANK_FUNCTION() OVER (
               PARTITION BY group_column
               ORDER BY metric DESC
           ) AS rank
    FROM aggregated_table
) t
WHERE rank <= N;

---

## 5️⃣ Common Use Cases

This pattern appears frequently in analytics problems:

- Top N customers per region
- Top N products per category
- Top N users per day
- Top N salespeople per quarter

Understanding ranking within partitions is essential for advanced SQL interviews.