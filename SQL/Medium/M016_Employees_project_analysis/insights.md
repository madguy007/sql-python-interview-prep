Step-by-step logic:
1. First, compute average hours per project.
2. Compare each employee’s hours with that project’s average.
3. Keep only rows where:
   hours > average_hours
4. Now, for each employee:
   count how many projects satisfy this condition.
5. If count > 1 → employee qualifies.

Why this approach works:
- The problem has two layers:
  (1) Row-level condition → compare with average
  (2) Group-level condition → count qualifying categories
- Filtering must happen BEFORE aggregation.

How to identify this type of problem (VERY IMPORTANT):

Look for these keywords in questions:
- "more than average"
- "greater than average per category"
- "in more than 1 / at least N categories"
- "for each group"

When you see this pattern, think:

Step 1 → Compute average per group (AVG + GROUP BY or WINDOW)
Step 2 → Filter rows using condition (WHERE)
Step 3 → GROUP BY entity (student, employee, business, etc.)
Step 4 → HAVING COUNT(DISTINCT category) > N

Mental template:
→ Filter first, then count valid categories

Common mistakes (what you were doing earlier):
- Counting before filtering ❌
- Using COUNT(*) instead of COUNT(DISTINCT category) ❌
- Grouping by extra columns ❌

Time Complexity:
- O(n log n) due to grouping

Key SQL concepts:
- Window Functions (AVG OVER)
- GROUP BY + HAVING
- COUNT(DISTINCT)
- Subquery / CTE
- Filtering order (WHERE before GROUP BY)