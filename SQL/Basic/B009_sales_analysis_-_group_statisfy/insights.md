This problem is not about filtering individual rows but about validating entire groups of rows for each product_id.

When we use GROUP BY product_id, all rows of that product are grouped together. The challenge is:
if even one row for that product lies outside the required date range, we must reject the whole group.

The key idea:
We are not asking “which rows are in range?”
We are asking “which products have ALL their rows in range?”

Why MIN and MAX works:
- MIN(sale_date) gives the earliest sale for that product
- MAX(sale_date) gives the latest sale for that product
- If both are within the Q1 range, then all intermediate dates must also be within range
- If even one sale is outside, MAX or MIN will go out of bounds and the product gets excluded

Why GROUP BY alone was causing confusion:
- GROUP BY combines multiple rows into one group
- But without proper HAVING conditions, it does not enforce constraints across all rows
- A CASE inside SUM without careful logic may still allow mixed valid/invalid rows

CASE-based solution logic:
- Count how many rows are outside the range
- If that count is 0, it means all rows are valid
- Otherwise, reject the product

NOT EXISTS approach:
- For each product, check if there exists any row outside the range
- If such a row exists → exclude
- If none exist → include

Core concept:
This is a group-level filtering problem where we ensure that no invalid rows exist inside a group.