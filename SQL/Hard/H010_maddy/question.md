Table: Activities

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+

There is no primary key and duplicates may exist.

Each row contains:
- sell_date → date product was sold
- product → product name

Write an SQL query to find for each date:
- Number of distinct products sold
- Product names sorted lexicographically and combined into one string

Return result ordered by sell_date.

Example Output:
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-Shirt|
| 2020-06-01 | 2        | Bible,Pencil                |
| 2020-06-02 | 1        | Mask                        |