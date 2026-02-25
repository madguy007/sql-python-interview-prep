WITH cte AS (
    SELECT user_id,
           login_date,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY login_date
           ) AS rn
    FROM Logins
)

SELECT user_id
FROM (
    SELECT user_id,
           login_date - rn * INTERVAL '1 day' AS grp
    FROM cte
) t
GROUP BY user_id, grp
HAVING COUNT(*) >= 3;
