SELECT 
    q.id,
    q.year,
    COALESCE(n.npv, 0) AS npv
FROM Queries AS q
LEFT JOIN NPV AS n
ON q.id = n.id 
AND q.year = n.year;

or 

SELECT 
    q.id,
    q.year,
    CASE
        WHEN n.npv IS NULL THEN 0
        ELSE n.npv
    END AS npv
FROM Queries AS q
LEFT JOIN NPV AS n
ON q.id = n.id 
AND q.year = n.year;
