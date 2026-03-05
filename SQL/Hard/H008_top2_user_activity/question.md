# Google SQL Interview Question

## Problem
Find the **top 2 most active users per day** based on the number of actions they performed.

## Table Structure

UserActivity(
    user_id,
    activity_date,
    action_id
)

## Requirements

1. Count the number of actions performed by each user per day.
2. Rank users **within each day** based on their action count.
3. Return the **top 2 users per day**.
4. If multiple users tie in rank, include all of them.

## Output

Return the following columns:

activity_date  
user_id  
action_count

## Example

Input:

| user_id | activity_date | action_id |
|--------|---------------|-----------|
| A | Jan1 | 1 |
| A | Jan1 | 2 |
| B | Jan1 | 3 |
| B | Jan1 | 4 |
| C | Jan1 | 5 |

Aggregated counts:

| user_id | activity_date | action_count |
|--------|---------------|-------------|
| A | Jan1 | 2 |
| B | Jan1 | 2 |
| C | Jan1 | 1 |

Top 2 ranks include A, B, and C because A and B tie for rank 1 and C gets rank 2.