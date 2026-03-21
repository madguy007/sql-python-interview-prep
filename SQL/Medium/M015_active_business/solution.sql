-- Step 1: Calculate avg occurrences per event_type
WITH avg_cte AS (
    SELECT 
        event_type,
        AVG(occurrences) AS avg_event
    FROM Events
    GROUP BY event_type
),

-- Step 2: Keep only rows where business beats avg
filtered AS (
    SELECT 
        e.business_id,
        e.event_type
    FROM Events e
    JOIN avg_cte a
      ON e.event_type = a.event_type
    WHERE e.occurrences > a.avg_event
)

-- Step 3: Business must satisfy condition for >1 event_type
SELECT business_id
FROM filtered
GROUP BY business_id
HAVING COUNT(event_type) > 1;


-- Alternative: Using window function (cleaner)

WITH cte AS (
    SELECT 
        business_id,
        event_type,
        occurrences,
        AVG(occurrences) OVER (PARTITION BY event_type) AS avg_event
    FROM Events
)

SELECT business_id
FROM cte
WHERE occurrences > avg_event
GROUP BY business_id
HAVING COUNT(event_type) > 1;