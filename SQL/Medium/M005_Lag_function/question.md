# Uber SQL Interview Question

## Problem

Find users who had at least one day where they made more transactions than the previous day.

## Table Structure

Transactions(
    transaction_id,
    user_id,
    transaction_date
)

## Requirements

1. Count number of transactions per user per day.
2. Compare each day's transaction count with the previous day’s count (for the same user).
3. If any day has strictly more transactions than the previous day → include that user.
4. Return:
   - user_id
