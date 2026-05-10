- GROUP BY sell_date groups all products sold on the same date.
- COUNT(DISTINCT product) removes duplicates and counts unique products.
- GROUP_CONCAT combines multiple product names into a single string.

Small GROUP_CONCAT Syntax:
- GROUP_CONCAT(column ORDER BY column SEPARATOR ',')

Purpose:
- Merges grouped row values into one comma-separated list
- ORDER BY ensures lexicographical sorting
- DISTINCT removes duplicate product names

Why useful:
- Converts multiple rows into readable aggregated text output

Key SQL Concepts:
- GROUP BY
- DISTINCT
- COUNT
- GROUP_CONCAT
- ORDER BY inside aggregation

This is a classic string aggregation interview pattern.