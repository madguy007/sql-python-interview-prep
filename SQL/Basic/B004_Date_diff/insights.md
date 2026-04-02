# Insights

## 1. Dealing With Dates in Different SQL Environments

Different SQL systems use different functions for date calculations.

| SQL System | Date Difference Syntax |
|------------|-----------------------|
| SQLite | julianday(date1) - julianday(date2) |
| MySQL | DATEDIFF(date1, date2) |
| PostgreSQL | date1 - date2 |
| SQL Server | DATEDIFF(day, date2, date1) |

Example (SQLite):

SELECT julianday('2023-01-10') - julianday('2023-01-01');

Output

9

---

## 2. What is julianday()

`julianday()` converts a date into a numeric day count (Julian day number).  
Because it returns a number, we can subtract two dates to find the difference.

Example

julianday('2023-01-10') = 2460000.5  
julianday('2023-01-01') = 2459991.5  

Difference

2460000.5 - 2459991.5 = 9

---

## 3. Extracting Year, Month, and Day

### SQLite
```
SELECT 
strftime('%Y', date_column) AS year,
strftime('%m', date_column) AS month,
strftime('%d', date_column) AS day,
strftime('%w',date_column) as Dayofweek
FROM table_name;
```
Example

SELECT strftime('%Y','2023-01-15');

Output

2023

---

### MySQL
```
SELECT 
YEAR(date_column),
MONTH(date_column),
DAY(date_column)
FROM table_name;
```
---

### PostgreSQL
```
SELECT 
EXTRACT(YEAR FROM date_column),
EXTRACT(MONTH FROM date_column),
EXTRACT(DAY FROM date_column)
FROM table_name;
```
---

## 4. Important SQLite Detail

`julianday()` returns a REAL (decimal) value.

Example output

9.0

Many SQL platforms expect an integer result, so we convert it using CAST.

CAST(julianday(EndDate) - julianday(StartDate) AS INTEGER)

---

## 5. Key Takeaways

- SQLite does not have DATEDIFF()
- Use julianday() to perform date calculations
- Convert results to INTEGER if needed
- Many SQL systems can automatically interpret YYYY-MM-DD text as a date
