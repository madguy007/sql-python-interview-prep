Table: Insurance

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+

Primary Key:
pid

Each row contains:
- pid → policy ID
- tiv_2015 → total investment value in 2015
- tiv_2016 → total investment value in 2016
- lat → latitude
- lon → longitude

Task:
Find the sum of tiv_2016 for policyholders who:
- Have tiv_2015 value repeated in other rows
- Have unique (lat, lon) location
- Return rounded to 2 decimal places