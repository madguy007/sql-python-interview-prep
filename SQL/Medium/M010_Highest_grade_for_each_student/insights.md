The task is to find the highest grade for each student and return the course associated with that grade. If multiple courses share the same highest grade, we must choose the course with the smallest course_id.

Each row in the Enrollments table represents a student's grade in a specific course. Since a student can have multiple rows, we must identify the best row per student.

Approach 1 uses a window function. The rows are partitioned by student_id, meaning each student's records are treated as a separate group. Inside each group, rows are ordered by grade in descending order so the highest grade appears first. If two courses have the same grade, ordering by course_id ascending ensures the smallest course_id appears first. The RANK() function assigns rank 1 to the best row per student, and filtering for rank = 1 returns the desired result.

Approach 2 first finds the maximum grade for each student using GROUP BY and MAX(). Then it joins this result back with the Enrollments table to retrieve the rows with that grade. If multiple rows match, another condition selects the smallest course_id among those tied grades.

Approach 3 compares rows within the same table using NOT EXISTS. For each row, SQL checks whether another row for the same student exists with either a higher grade or the same grade but a smaller course_id. If such a row exists, the current row cannot be the best one. Rows for which no better row exists are returned.

Important SQL concepts used:
- Window functions with PARTITION BY and ORDER BY
- Ranking functions such as RANK()
- Aggregation using GROUP BY and MAX()
- Self comparison using NOT EXISTS
- Tie-breaking logic using ORDER BY or MIN(course_id)