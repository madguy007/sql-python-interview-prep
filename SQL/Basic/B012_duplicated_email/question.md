Given a table of employees with columns such as employee_id, name, and email, 
write a Python program to find the employee records where the email is duplicated 
(i.e., more than one employee has the same email).

From those duplicate email groups, return the employee with the maximum employee_id 
for each duplicated email.

Example Input:
employees = [
    {"employee_id": 1, "name": "A", "email": "a@gmail.com"},
    {"employee_id": 2, "name": "B", "email": "b@gmail.com"},
    {"employee_id": 3, "name": "C", "email": "a@gmail.com"},
    {"employee_id": 4, "name": "D", "email": "c@gmail.com"},
    {"employee_id": 5, "name": "E", "email": "b@gmail.com"}
]

Example Output:
[
    {"employee_id": 3, "name": "C", "email": "a@gmail.com"},
    {"employee_id": 5, "name": "E", "email": "b@gmail.com"}
]