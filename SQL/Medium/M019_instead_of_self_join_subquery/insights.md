- This problem combines:
  1. Duplicate value filtering
  2. Unique location filtering

Main challenge:
- We must compare rows against the full dataset
- Direct self joins can become complicated

Simpler strategy:
- Use subqueries to precompute valid groups
- Then filter main table

Step 1:
Find repeated tiv_2015 values:
GROUP BY tiv_2015
HAVING COUNT(*) > 1

Step 2:
Find unique locations:
GROUP BY lat, lon
HAVING COUNT(*) = 1

Step 3:
Filter original table using IN conditions

Why easier:
- Avoids row-by-row comparisons
- Cleaner than self join
- More readable interview solution

Pattern Recognition:
- Duplicate values:
  HAVING COUNT(*) > 1
- Unique values:
  HAVING COUNT(*) = 1

Important SQL Concept:
(lat, lon) IN (...)
- Composite tuple filtering
- Allows checking multi-column uniqueness

Why powerful:
- Modular logic
- Easy debugging
- Reusable for many duplicate + unique condition problems

Key SQL Concepts:
- GROUP BY
- HAVING
- COUNT(*)
- Subqueries
- IN
- Composite filtering
- SUM
- ROUND

Memory Rule:
Need repeated values?
→ HAVING COUNT(*) > 1

Need unique values?
→ HAVING COUNT(*) = 1

This is a classic duplicate-detection + subquery-filtering interview pattern.