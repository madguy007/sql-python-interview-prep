-- Approach 1: Using CTE + NOT IN (Clean and intuitive)
WITH CTE AS (
    SELECT activity, COUNT(*) AS cnt
    FROM Friends
    GROUP BY activity
)
SELECT activity
FROM CTE
WHERE cnt NOT IN (
    SELECT MAX(cnt) FROM CTE
    UNION ALL
    SELECT MIN(cnt) FROM CTE
);

-- Approach 2: Using HAVING with subqueries
SELECT activity
FROM Friends
GROUP BY activity
HAVING COUNT(*) NOT IN (
    (SELECT MAX(cnt) FROM (
        SELECT COUNT(*) AS cnt
        FROM Friends
        GROUP BY activity
    )),
    (SELECT MIN(cnt) FROM (
        SELECT COUNT(*) AS cnt
        FROM Friends
        GROUP BY activity
    ))
);

-- Approach 3: Using Window Functions
WITH CTE AS (
    SELECT 
        activity,
        COUNT(*) AS cnt,
        MAX(COUNT(*)) OVER () AS max_cnt,
        MIN(COUNT(*)) OVER () AS min_cnt
    FROM Friends
    GROUP BY activity
)
SELECT activity
FROM CTE
WHERE cnt != max_cnt AND cnt != min_cnt;