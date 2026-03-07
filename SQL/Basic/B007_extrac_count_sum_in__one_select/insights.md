# Insight

In this problem we use multiple aggregate functions inside a single SELECT statement.

Functions used:

COUNT() → to count number of orders  
SUM() → to calculate total revenue  
EXTRACT() → to get the month from a date column

Example:

EXTRACT(MONTH FROM order_date)

This extracts the month number from the order date.

SQL allows us to use multiple aggregate functions in one query like this:

SELECT
COUNT(...),
SUM(...)

When we use aggregate functions together with non-aggregated columns, we must use GROUP BY.

GROUP BY groups rows based on a column or expression.  
Here we group by the month extracted from order_date so that revenue and order count are calculated for each month.

ENd