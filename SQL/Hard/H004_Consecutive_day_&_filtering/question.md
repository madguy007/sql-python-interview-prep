# Stripe SQL Interview Question

## Problem

Find users who had:

- Transactions on **at least 3 consecutive calendar days**
- AND the **total transaction amount across those 3 consecutive days is greater than 1000**

## Table Structure

Transactions(
    transaction_id,
    user_id,
    transaction_date,
    amount
)

## Requirements

- Consecutive means calendar consecutive (e.g., Jan 1, Jan 2, Jan 3).
- If a user has multiple streaks, and any one 3-day streak exceeds 1000 → include that user.
- Return only:
    user_id
