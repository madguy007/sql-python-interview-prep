==================================================
DDL (Data Definition Language)
==================================================

Purpose:
- Defines or changes database structure

Commands:

1. CREATE
- Creates new database/table

Example:
CREATE TABLE Employee (
    employee_id INT,
    name VARCHAR(50),
    salary INT
);

2. ALTER
- Modifies existing table structure

Example:
ALTER TABLE Employee
ADD department VARCHAR(50);

3. DROP
- Deletes entire table/database

Example:
DROP TABLE Employee;

4. TRUNCATE
- Removes all rows, keeps structure

Example:
TRUNCATE TABLE Employee;

--------------------------------------------------

Memory Rule:
DDL = Structure Commands

CREATE → New structure
ALTER → Modify structure
DROP → Delete structure
TRUNCATE → Clear data only

==================================================
DML (Data Manipulation Language)
==================================================

Purpose:
- Works with actual data inside tables

Commands:

1. INSERT
- Adds new records

Example:
INSERT INTO Employee (employee_id, name, salary)
VALUES (101, 'Maddy', 50000);

2. UPDATE
- Modifies existing records

Example:
UPDATE Employee
SET salary = 75000
WHERE employee_id = 101;

3. DELETE
- Removes specific records

Example:
DELETE FROM Employee
WHERE employee_id = 101;

--------------------------------------------------

Memory Rule:
DML = Data Commands

INSERT → Add data
UPDATE → Change data
DELETE → Remove data

==================================================
Quick Difference
==================================================

DDL:
- Changes table design
- Auto-commits in many DBMS

DML:
- Changes table data
- Can often be rolled back

==================================================
Interview Shortcut
==================================================

Structure?
→ DDL

Data?
→ DML

==================================================
Core Beginner SQL Foundation:
==================================================

DDL = Database blueprint
DML = Database content