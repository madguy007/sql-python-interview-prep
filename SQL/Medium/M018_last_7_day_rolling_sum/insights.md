- GROUP BY visited_on -> creates daily total sales
- SUM(day_amount) OVER(...) -> rolling 7-day revenue
- AVG(day_amount) OVER(...) -> rolling 7-day average
- OFFSET 6 -> removes incomplete first 6 days


===ROWS BETWEEN FRAME LOGIC===
ROWS BETWEEN 6 PRECEDING AND CURRENT ROW

Meaning:
For each row:
- Take current row
- Take previous 6 rows
- Total frame size = 7 rows

Example:
Day7:
[Day1 Day2 Day3 Day4 Day5 Day6 Day7]

Day8:
[Day2 Day3 Day4 Day5 Day6 Day7 Day8]

Day9:
[Day3 Day4 Day5 Day6 Day7 Day8 Day9]

This creates a sliding window.


===PURPOSE===
- Fixed-size rolling calculations
- Moving averages
- Running totals over specific periods


===KEY SQL CONCEPTS===
- CTE
- GROUP BY
- WINDOW FUNCTIONS
- ORDER BY
- ROWS BETWEEN
- SUM
- AVG
- ROUND
- OFFSET


===KEY RULE===
ROWS BETWEEN N PRECEDING AND CURRENT ROW
-> Creates rolling frame of N+1 rows


===PATTERN TYPE===
Classic Sliding Window / Moving Average SQL Question