# Meta (Facebook) SQL Interview Question

## Problem
Find users who had **at least 3 consecutive days where their daily number of actions increased compared to the previous day**.

## Table Structure

UserActivity(
    user_id,
    activity_date,
    action_id
)

## Requirements

1. First compute the **daily number of actions per user**.
2. Compare each day's action count with the **previous day's count**.
3. Detect **streaks where the number of actions keeps increasing**.
4. If a user has **3 consecutive increasing days**, include that user.

## Output

Return:

user_id

## Example

| user_id | activity_date | action_id |
|--------|---------------|-----------|
| A | Jan1 | 1 |
| A | Jan1 | 2 |
| A | Jan2 | 3 |
| A | Jan2 | 4 |
| A | Jan2 | 5 |
| A | Jan3 | 6 |
| A | Jan3 | 7 |
| A | Jan3 | 8 |
| A | Jan3 | 9 |

Daily counts:

| date | actions |
|------|--------|
| Jan1 | 2 |
| Jan2 | 3 |
| Jan3 | 4 |
| Jan4 | 6 |

Action increases:

2 → 3 ↑  
3 → 4 ↑  
4 → 6 ↑  

User A qualifies.