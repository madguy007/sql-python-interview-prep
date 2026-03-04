# Subscription Duration Calculation (SQLite)

## Problem
Given a table `Subscriptions`, calculate the total number of days each subscription lasted.

The duration is the difference between `EndDate` and `StartDate`.

Return the result with the following columns:

- `id`
- `SubscriptionDays`

## Table: Subscriptions

| Column | Type |
|------|------|
| id | INTEGER |
| StartDate | TEXT |
| EndDate | TEXT |

Dates are stored in **text format (`YYYY-MM-DD`)**.

## Example

### Input

| id | StartDate | EndDate |
|----|-----------|---------|
| 1 | 2023-01-01 | 2023-01-10 |
| 2 | 2023-02-01 | 2023-02-15 |

### Output

| id | SubscriptionDays |
|----|------------------|
| 1 | 9 |
| 2 | 14 |

## Explanation

Subscription days are calculated as:
