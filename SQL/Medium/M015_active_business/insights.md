Step-by-step logic:
1. Compute average occurrences per event_type.
2. Compare each business's occurrences with that average.
3. Keep only rows where:
   occurrences > average
4. For each business:
   count how many event_types satisfy this condition.
5. If count > 1 → active business.

Why your approach failed:
- You counted total rows per business instead of valid event_types.
- You didn’t filter using the main condition (occurrences > avg).
- Filtering must happen BEFORE grouping.

Key intuition:
This is a **2-layer filtering problem**:
1. Row-level filter → compare with average
2. Group-level filter → count valid event_types

Time Complexity:
- O(n log n) due to grouping

Key SQL concepts:
- Window functions (AVG OVER)
- GROUP BY + HAVING
- Filtering before aggregation
- Join vs Window optimization

Interview tip:
Whenever you see:
"more than one category satisfying a condition"

Think:
→ Filter first → then GROUP BY → HAVING COUNT > 1