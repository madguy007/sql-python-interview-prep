# Replace NULL with 0 (SQL)

You are given two tables.
```
### Queries
| id | year |
|----|------|

### NPV
| id | year | npv |
|----|------|-----|
```
Write an SQL query to find the **NPV value for each (id, year) pair present in the Queries table**.

If the corresponding `(id, year)` pair does not exist in the `NPV` table, return **0** as the NPV value.

Return the result table in any order.

### Example

**Input**
```
Queries

| id | year |
|----|------|
| 1  | 2019 |
| 2  | 2008 |
| 3  | 2009 |
| 7  | 2018 |
| 7  | 2019 |
| 7  | 2020 |
| 13 | 2019 |

NPV

| id | year | npv |
|----|------|-----|
| 1  | 2019 | 113 |
| 2  | 2008 | 121 |
| 3  | 2009 | 21 |
| 7  | 2019 | 0 |
| 7  | 2020 | 30 |
| 13 | 2019 | 40 |

**Output**

| id | year | npv |
|----|------|-----|
| 1  | 2019 | 113 |
| 2  | 2008 | 121 |
| 3  | 2009 | 21 |
| 7  | 2018 | 0 |
| 7  | 2019 | 0 |
| 7  | 2020 | 30 |
| 13 | 2019 | 40 |
```
