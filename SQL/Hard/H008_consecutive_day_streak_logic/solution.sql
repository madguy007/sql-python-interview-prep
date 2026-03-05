-- Step 1: Compute daily action counts

WITH daily_actions AS (
    SELECT
        user_id,
        activity_date,
        COUNT(*) AS action_count
    FROM UserActivity
    GROUP BY user_id, activity_date
),

-- Step 2: Detect increases compared to previous day

price_changes AS (
    SELECT
        user_id,
        activity_date,
        action_count,
        CASE
            WHEN action_count > LAG(action_count) OVER (
                PARTITION BY user_id
                ORDER BY activity_date
            )
            THEN 1 ELSE 0
        END AS inc
    FROM daily_actions
),

-- Step 3: Create groups for consecutive increase streaks

grp AS (
    SELECT
        user_id,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY activity_date
        )
        -
        ROW_NUMBER() OVER (
            PARTITION BY user_id, inc
            ORDER BY activity_date
        ) AS g
    FROM price_changes
    WHERE inc = 1
)

-- Step 4: Detect streak length

SELECT user_id
FROM grp
GROUP BY user_id, g
HAVING COUNT(*) >= 3;