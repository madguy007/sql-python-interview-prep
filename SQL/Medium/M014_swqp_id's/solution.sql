-- Approach 1: Using CASE + COUNT (Most common solution)

select case when id % 2 = 1 and id != (select max(id) from Seat) then id+1
            when id % 2 = 0 then id-1
            else id end as id, student
from Seat
order by id


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
