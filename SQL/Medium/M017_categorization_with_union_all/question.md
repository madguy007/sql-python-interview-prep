Table: Accounts

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+

account_id is the primary key.

Salary Categories:
- Low Salary → income < 20000
- Average Salary → income BETWEEN 20000 AND 50000
- High Salary → income > 50000

Write an SQL query to count the number of accounts in each category.

Requirements:
- Must return all 3 categories
- If no accounts exist in a category → return 0

Example:

Input:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+

Output:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |