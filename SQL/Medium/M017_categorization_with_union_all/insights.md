Problem Type:
- Fixed category segmentation problem
- Categories are manually defined by business rules
- Need guaranteed rows even when category count is zero

Core Logic:
- Low Salary count
- Average Salary count
- High Salary count
- Combine all results vertically

Why UNION ALL is Ideal:
- Each category has separate filtering logic
- Each category is independently aggregated
- All categories must always appear
- Zero-count categories are preserved
- Cleaner than CASE + GROUP BY
- Easier readability

Traditional GROUP BY Difficulty:
- Categories are not naturally stored as data values
- Requires CASE statements
- Missing categories may disappear
- More complex handling for zero rows

Example GROUP BY alternative:
CASE
  WHEN income < 20000 THEN 'Low Salary'
  WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
  ELSE 'High Salary'
END

Problems:
- Can miss empty categories
- More verbose
- Less explicit

Why UNION ALL is Better:
- Manual row construction
- Predictable structure
- Cleaner interview explanation
- Better for fixed-output problems

How to Identify UNION ALL Problems:
Use UNION ALL when:
1. Problem asks for exact predefined categories
2. Multiple separate conditions exist
3. Each category requires independent aggregation
4. Output structure is fixed
5. Zero-count rows must still be returned

Common Examples:
- Salary bands
- Pass/Fail
- Revenue buckets
- Age groups
- Customer segmentation
- Order ranges

UNION vs UNION ALL:
- UNION removes duplicates
- UNION ALL keeps all rows
- UNION ALL is faster
- Use UNION ALL when categories are already distinct

Shortcut Recognition:
If problem says:
"Return these exact categories"

Think:
- Separate SELECT statements
- Separate WHERE clauses
- Stack results with UNION ALL

Key SQL Concepts:
- UNION ALL
- Conditional aggregation
- Fixed business categories
- Manual output construction
- Guaranteed category completeness

Summary:
GROUP BY:
- Use when categories naturally exist in data

UNION ALL:
- Use when categories are manually defined

Final Pattern:
Fixed custom buckets
→ Separate conditions
→ Separate SELECTs
→ UNION ALL