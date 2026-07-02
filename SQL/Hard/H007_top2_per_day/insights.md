# Top Two Activity Ranks per Day

This problem has two separate steps: aggregate the actions and then rank the
aggregated results. Ranking the original activity rows would rank individual
events rather than users.

`GROUP BY user_id, activity_date` produces one row per user per day, while
`COUNT(*)` calculates that user's activity level. The second CTE applies
`DENSE_RANK()` with `PARTITION BY activity_date`, so ranking restarts for every
day and orders users by their action count from highest to lowest.

`DENSE_RANK()` is important because ties share a rank without creating gaps.
Filtering with `rnk <= 2` therefore returns the top two distinct activity
levels and may correctly return more than two users when ties occur.
