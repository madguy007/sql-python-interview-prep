-- Step 1: Count number of actions per user per day

WITH activity_counts AS (
    SELECT
        user_id,
        activity_date,
        COUNT(*) AS action_count
    FROM UserActivity
    GROUP BY user_id, activity_date
),

-- Step 2: Rank users within each day based on activity count

ranked_users AS (
    SELECT
        user_id,
        activity_date,
        action_count,
        DENSE_RANK() OVER (
            PARTITION BY activity_date
            ORDER BY action_count DESC
        ) AS rnk
    FROM activity_counts
)

-- Step 3: Keep only top 2 ranks

SELECT
    activity_date,
    user_id,
    action_count
FROM ranked_users
WHERE rnk <= 2;