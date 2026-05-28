Assume you're given a table containing data on Amazon customers and their spending on products in different categories.

Write an SQL query to identify the top two highest-grossing products within each category in the year 2022.

The output should include:
- category
- product
- total spend

Table: product_spend

+------------------+-----------+
| Column Name      | Type      |
+------------------+-----------+
| category         | string    |
| product          | string    |
| user_id          | integer   |
| spend            | decimal   |
| transaction_date | timestamp |
+------------------+-----------+

Example Input:

| category    | product           | user_id | spend  | transaction_date   |
|-------------|------------------|----------|---------|--------------------|
| appliance   | refrigerator      | 165      | 246.00  | 12/26/2021         |
| appliance   | refrigerator      | 123      | 299.99  | 03/02/2022         |
| appliance   | washing machine   | 123      | 219.80  | 03/02/2022         |
| electronics | vacuum            | 178      | 152.00  | 04/05/2022         |
| electronics | wireless headset  | 156      | 249.90  | 07/08/2022         |
| electronics | vacuum            | 145      | 189.00  | 07/15/2022         |

==================================================