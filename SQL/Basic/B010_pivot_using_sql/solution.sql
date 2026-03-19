-- Approach 1: Using CASE WHEN + Aggregation (Most Common)
SELECT 
    id,
    SUM(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,
    SUM(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,
    SUM(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue,
    SUM(CASE WHEN month = 'Apr' THEN revenue END) AS Apr_Revenue,
    SUM(CASE WHEN month = 'May' THEN revenue END) AS May_Revenue,
    SUM(CASE WHEN month = 'Jun' THEN revenue END) AS Jun_Revenue,
    SUM(CASE WHEN month = 'Jul' THEN revenue END) AS Jul_Revenue,
    SUM(CASE WHEN month = 'Aug' THEN revenue END) AS Aug_Revenue,
    SUM(CASE WHEN month = 'Sep' THEN revenue END) AS Sep_Revenue,
    SUM(CASE WHEN month = 'Oct' THEN revenue END) AS Oct_Revenue,
    SUM(CASE WHEN month = 'Nov' THEN revenue END) AS Nov_Revenue,
    SUM(CASE WHEN month = 'Dec' THEN revenue END) AS Dec_Revenue
FROM Department
GROUP BY id;

-- Approach 2: Using FILTER (PostgreSQL specific, cleaner)
SELECT 
    id,
    SUM(revenue) FILTER (WHERE month = 'Jan') AS Jan_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Feb') AS Feb_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Mar') AS Mar_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Apr') AS Apr_Revenue,
    SUM(revenue) FILTER (WHERE month = 'May') AS May_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Jun') AS Jun_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Jul') AS Jul_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Aug') AS Aug_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Sep') AS Sep_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Oct') AS Oct_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Nov') AS Nov_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Dec') AS Dec_Revenue
FROM Department
GROUP BY id;

-- Approach 3: Using PIVOT (SQL Server)
SELECT *
FROM (
    SELECT id, month, revenue
    FROM Department
) AS src
PIVOT (
    SUM(revenue)
    FOR month IN (
        [Jan], [Feb], [Mar], [Apr], [May], [Jun],
        [Jul], [Aug], [Sep], [Oct], [Nov], [Dec]
    )
) AS pvt;