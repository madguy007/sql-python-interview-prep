Exchange Seats

Write a SQL query to swap the seat id of every two consecutive students. 
If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

Table: Seat

Columns:
- id (int, primary key, continuous increment)
- student (string)

Each row represents a student sitting on a seat.

Example:

Input:
Seat table:
id | student
1  | A
2  | B
3  | C
4  | D
5  | E

Output:
id | student
1  | B
2  | A
3  | D
4  | C
5  | E