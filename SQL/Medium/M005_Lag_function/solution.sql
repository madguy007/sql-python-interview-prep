-- ======================================
-- Step 1: Aggregate daily transactions
-- ======================================

WITH cte1 AS (
    SELECT user_id,
           transaction_date,
           COUNT(*) AS curr_t
    FROM Transactions
    GROUP BY user_id, transaction_date
),

-- ======================================
-- Step 2: Use LAG to compare with previous day
-- ======================================

cte2 AS (
    SELECT user_id,
           transaction_date,
           curr_t,
           LAG(curr_t) OVER (
               PARTITION BY user_id
               ORDER BY transaction_date
           ) AS prev_t
    FROM cte1
)

-- ======================================
-- Step 3: Filter users with increase
-- ======================================

SELECT DISTINCT user_id
FROM cte2
WHERE curr_t > prev_t;
