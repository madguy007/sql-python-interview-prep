- NULL represents missing, unknown, or undefined data.
- It is NOT equal to 0, empty string, or FALSE.

Important Rule:
- NULL cannot be checked using = NULL
- Always use:
  IS NULL
  IS NOT NULL

Example:
Incorrect:
salary = NULL

Correct:
salary IS NULL

==================================
Common NULL Handling Techniques
==================================

1. IS NULL
- Finds missing values

Example:
WHERE manager_id IS NULL

--------------------------------------------------

2. IS NOT NULL
- Finds existing values

Example:
WHERE manager_id IS NOT NULL

--------------------------------------------------

3. COALESCE()
- Replaces NULL with first non-null value

Syntax:
COALESCE(column, replacement)

Example:
COALESCE(phone_number, 'Not Provided')

--------------------------------------------------

4. IFNULL() (MySQL)
- Similar to COALESCE for two values

Example:
IFNULL(phone_number, 'Not Provided')

--------------------------------------------------

5. Aggregation Functions
- SUM(), AVG(), COUNT(column) ignore NULLs automatically

Example:
AVG(salary)

Important:
COUNT(*) counts all rows
COUNT(column) ignores NULL rows

--------------------------------------------------

6. CASE Statement
- Custom NULL categorization

Example:
CASE WHEN salary IS NULL THEN 'Unknown'

==================================================
Interview Memory Rules
==================================================

Missing value?
→ IS NULL

Replace missing value?
→ COALESCE()

MySQL replacement?
→ IFNULL()

Conditional handling?
→ CASE

==================================================
Key SQL Concepts:
==================================================

- NULL
- IS NULL
- IS NOT NULL
- COALESCE
- IFNULL
- CASE
- Aggregate behavior

==================================================
Core Insight:
==================================================

NULL handling is critical because:
- Comparisons fail
- Aggregations behave differently
- Reporting can break without replacements

Strong NULL handling improves:
- Data quality
- Reporting accuracy
- Interview performance
