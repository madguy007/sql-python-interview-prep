-- Approach 1: Window Function (Recommended)
SELECT student_id, course_id, grade
FROM (
        SELECT 
            student_id,
            course_id,
            grade,
            RANK() OVER (
                PARTITION BY student_id 
                ORDER BY grade DESC, course_id ASC
            ) AS rnk
        FROM Enrollments
     ) t
WHERE rnk = 1
ORDER BY student_id;


-- Approach 2: Using Subquery with MAX Grade
SELECT e.student_id, e.course_id, e.grade
FROM Enrollments e
JOIN (
        SELECT student_id, MAX(grade) AS max_grade
        FROM Enrollments
        GROUP BY student_id
     ) m
ON e.student_id = m.student_id
AND e.grade = m.max_grade
WHERE e.course_id = (
        SELECT MIN(course_id)
        FROM Enrollments
        WHERE student_id = e.student_id
        AND grade = m.max_grade
)
ORDER BY e.student_id;


-- Approach 3: Using NOT EXISTS (Self Comparison)
SELECT e1.student_id, e1.course_id, e1.grade
FROM Enrollments e1
WHERE NOT EXISTS (
        SELECT 1
        FROM Enrollments e2
        WHERE e1.student_id = e2.student_id
        AND (
            e2.grade > e1.grade
            OR (e2.grade = e1.grade AND e2.course_id < e1.course_id)
        )
)
ORDER BY e1.student_id;