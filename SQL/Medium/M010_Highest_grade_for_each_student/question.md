Table: Enrollments

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student_id  | int     |
| course_id   | int     |
| grade       | int     |
+-------------+---------+

(student_id, course_id) is the primary key for this table.
Each row indicates that a student received a grade in a specific course.

Write a SQL query to find the highest grade with its corresponding course for each student.

If a student has multiple courses with the same highest grade, return the course with the smallest course_id.

Return the result table ordered by student_id in ascending order.

The result should contain:
student_id | course_id | grade