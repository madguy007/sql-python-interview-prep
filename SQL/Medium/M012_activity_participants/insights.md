1. Core idea:
   - First, convert raw data into aggregated form:
     → count number of participants per activity

2. The tricky part (important learning):
   - Once we have cnt (count per activity), we need to compare it with:
     → maximum count
     → minimum count
   - But both max and min are derived from the SAME aggregated column (cnt)

3. Key insight from this solution:
   - We reuse the same CTE result to compute:
     → MAX(cnt)
     → MIN(cnt)
   - Then filter using:
     → cnt NOT IN (max, min)

4. Why this works well:
   - CTE acts like a temporary table
   - Avoids recomputing counts multiple times
   - Keeps logic clean and readable

5. Important interview pattern:
   - When comparing a value against aggregate of same column:
     → First compute aggregation (CTE / subquery)
     → Then apply aggregate functions (MAX, MIN) on that result

6. Conceptual flow:
   Step 1 → GROUP BY activity → get cnt
   Step 2 → Find MAX(cnt) and MIN(cnt)
   Step 3 → Filter out those extremes

7. SQL concepts used:
   - GROUP BY + COUNT
   - CTE (Common Table Expression)
   - Subquery with UNION ALL
   - Filtering using NOT IN
   - Window functions (alternative approach)