# Insights – 3 Consecutive Login Days

## Concept Tested
This is a classic "Gaps and Islands" problem.

The challenge is detecting consecutive date sequences.

---

## Why ROW_NUMBER() is Used

ROW_NUMBER() assigns increasing numbers per user ordered by login_date.
```
Example:

login_date | rn
2024-01-10 | 1
2024-01-11 | 2
2024-01-13 | 3
2024-01-14 | 4
2024-01-15 | 5
```
---

## The Core Trick

We compute:

login_date - rn

Why?

In consecutive sequences:
- login_date increases by 1
- rn increases by 1
- Their difference stays constant

Example:
```
Date | rn | Date - rn
10   | 1  | 9
11   | 2  | 9
12   | 3  | 9
```
Same value → same group.

When a gap happens:
```
Date | rn | Date - rn
13   | 3  | 10
```
Value changes → new group.

---

## Final Logic

1. Assign row_number per user ordered by date
2. Subtract rn from login_date
3. Group by that derived value
4. If count >= 3 → user qualifies

---

## What This Question Tests

- Window functions
- Date arithmetic
- Pattern recognition
- Handling sequence breaks
- Real interview-level SQL thinking
