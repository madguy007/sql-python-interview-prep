-- Approach 1: Using CASE + COUNT (Most common solution)

SELECT 
    CASE
        WHEN id % 2 = 1 AND id != counts THEN id + 1
        WHEN id % 2 = 1 AND id = counts THEN id
        ELSE id - 1
    END AS id,
    student
FROM Seat,
     (SELECT COUNT(*) AS counts FROM Seat) AS seat_counts
ORDER BY id;


-- Approach 2: Using LEAD and LAG (Window Functions)

SELECT 
    CASE 
        WHEN id % 2 = 1 AND LEAD(student) OVER (ORDER BY id) IS NOT NULL 
            THEN LEAD(student) OVER (ORDER BY id)
        WHEN id % 2 = 0 
            THEN LAG(student) OVER (ORDER BY id)
        ELSE student
    END AS student,
    id
FROM Seat
ORDER BY id;