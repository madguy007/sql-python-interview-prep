-- Step 1: Get first login date per user
-- Step 2: Filter last 90 days
-- Step 3: Count users per date

SELECT 
    first_login AS login_date,
    COUNT(*) AS user_count
FROM (
    SELECT 
        user_id,
        MIN(activity_date) AS first_login
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id
) t
WHERE first_login BETWEEN DATE('2019-06-30', '-90 day') AND DATE('2019-06-30')
GROUP BY first_login;

-- Alternative Approach: Using Window Function (if supported)
SELECT 
    activity_date AS login_date,
    COUNT(*) AS user_count
FROM (
    SELECT 
        user_id,
        activity_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date) AS rn
    FROM Traffic
    WHERE activity = 'login'
) t
WHERE rn = 1
  AND activity_date BETWEEN DATE('2019-06-30', '-90 day') AND DATE('2019-06-30')
GROUP BY activity_date;