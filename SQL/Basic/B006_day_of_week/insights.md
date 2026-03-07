# Insight

This problem tests understanding of **date functions in SQL**.

## How to Get Day From a Date

Different SQL databases use different functions to extract the **day of the week**.

---

## MySQL

Function:

DAYOFWEEK(date)

Example:

SELECT DAYOFWEEK('2024-06-16');

Return values:

| Day | Value |
|-----|------|
| Sunday | 1 |
| Monday | 2 |
| Tuesday | 3 |
| Wednesday | 4 |
| Thursday | 5 |
| Friday | 6 |
| Saturday | 7 |

### Weekend Logic

Weekend days are:

Sunday → 1  
Saturday → 7  

Query logic:

DAYOFWEEK(hire_date) IN (1,7)

---

## PostgreSQL

Function:

EXTRACT(DOW FROM date)

Example:

SELECT EXTRACT(DOW FROM DATE '2024-06-16');

Return values:

| Day | Value |
|-----|------|
| Sunday | 0 |
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4 |
| Friday | 5 |
| Saturday | 6 |

### Weekend Logic

Weekend days:

Sunday → 0  
Saturday → 6  

Query logic:

EXTRACT(DOW FROM hire_date) IN (0,6)

---

## SQLite

Function:

strftime('%w', date)

Example:

SELECT strftime('%w', '2024-06-16');

Return values:

| Day | Value |
|-----|------|
| Sunday | 0 |
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4 |
| Friday | 5 |
| Saturday | 6 |

### Weekend Logic

Weekend days:

Sunday → 0  
Saturday → 6  

Query logic:

strftime('%w', hire_date) IN ('0','6')

---

## Key Concept

Date functions allow us to extract useful information from dates such as:

- day of week
- month
- year
- week number

These functions are commonly used in **analytics, reporting, and business logic queries**.