-- Solution 1 : Self Join Approach

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2
ON l1.id = l2.id - 1
JOIN Logs l3
ON l2.id = l3.id - 1
WHERE l1.num = l2.num
AND l2.num = l3.num;


-- Solution 2 : Window Function Approach

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num,1) OVER(ORDER BY id) AS prev1,
        LAG(num,2) OVER(ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1
AND num = prev2;