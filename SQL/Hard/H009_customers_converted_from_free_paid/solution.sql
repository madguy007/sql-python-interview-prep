-- Approach: Using LEAD + GROUP BY + WINDOW FUNCTION

SELECT 
    next_plan,
    COUNT(*) AS conversions,
    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS conversion_percentage
FROM (
    SELECT 
        customer_id,
        plan_id,
        LEAD(plan_id) OVER (
            PARTITION BY customer_id 
            ORDER BY start_date
        ) AS next_plan
    FROM subscriptions
) t
WHERE plan_id = 0 
  AND next_plan != 0
GROUP BY next_plan
ORDER BY next_plan;