Step-by-step logic:
1. Use LEAD() to find the next plan for each customer.
2. Filter only rows where:
   - current plan = free trial (plan_id = 0)
   - next_plan is a paid plan
3. Group by next_plan to count how many customers converted to each plan.
4. Calculate percentage using total conversions.

Key Concept: COUNT(*) vs SUM(COUNT(*)) OVER ()

- COUNT(*) gives:
  → number of rows per group (per plan)

Example after GROUP BY:

| plan | COUNT(*) |
|------|----------|
| 1    | 3        |
| 2    | 2        |

- SUM(COUNT(*)) OVER () gives:
  → total across ALL groups

| plan | count | total |
|------|------|-------|
| 1    | 3    | 5     |
| 2    | 2    | 5     |

Explanation:
- COUNT(*) is computed after GROUP BY (per group)
- OVER() turns SUM into a window function
- OVER() means:
  "apply this function across all rows without collapsing them"

So:
SUM(COUNT(*)) OVER ()
= sum of all group counts
= total number of converted customers

Important Understanding of OVER():
- Without OVER():
  SUM(COUNT(*)) → invalid (nested aggregate not allowed)
- With OVER():
  SUM(COUNT(*)) OVER ()
  → runs AFTER grouping
  → creates a new column containing total value repeated for each row

Mental Model:
- GROUP BY → reduces rows
- OVER() → does NOT reduce rows, it adds information

Why this approach works:
- We first identify valid conversions (free → paid)
- Then count per plan
- Then compute total dynamically using window function
- No separate subquery needed for total

Time Complexity:
- O(n log n) due to grouping and window functions

Key SQL concepts:
- Window Functions (LEAD, SUM OVER)
- GROUP BY + HAVING logic
- COUNT(*)
- OVER() behavior
- Partitioning vs grouping

Interview Tip:
Whenever you need:
"percentage distribution across groups"

Think:
→ COUNT(*) / SUM(COUNT(*)) OVER ()