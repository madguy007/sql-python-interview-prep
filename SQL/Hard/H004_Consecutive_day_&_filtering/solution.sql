WITH cte1 AS (
    -- Step 1: Aggregate multiple transactions on the same day
    SELECT user_id,
           transaction_date,
           SUM(amount) AS daily_amount
    FROM Transactions
    GROUP BY user_id, transaction_date
),
cte2 AS (
    -- Step 2: Assign row numbers per user ordered by date
    SELECT user_id,
           transaction_date,
           daily_amount,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY transaction_date
           ) AS rn
    FROM cte1
),
cte3 AS (
    -- Step 3: Create grouping key for consecutive dates
    SELECT user_id,
           transaction_date - rn * INTERVAL '1 day' AS grp,
           daily_amount
    FROM cte2
)
-- Step 4: Filter valid streaks
SELECT user_id
FROM cte3
GROUP BY user_id, grp
HAVING COUNT(*) >= 3
   AND SUM(daily_amount) > 1000;
