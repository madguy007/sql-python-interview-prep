SELECT 
    m.name,
    SUM(
        CASE
            WHEN e.managerId IS NOT NULL THEN 1
            ELSE 0
        END
    ) AS direct_report
FROM Employee AS e
JOIN Employee AS m
ON e.managerId = m.id
GROUP BY m.name;