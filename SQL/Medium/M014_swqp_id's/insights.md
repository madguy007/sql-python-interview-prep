Step-by-step logic:
1. We need to swap every pair of rows: (1↔2), (3↔4), etc.
2. Odd IDs move to next (id + 1), even IDs move to previous (id - 1).
3. Special case: If total rows are odd, last row should not move.

Approach 1 (CASE + COUNT):
- Use id % 2 to detect odd/even rows.
- If id is odd → normally swap with next (id + 1).
- But if it's the last row (id = total count), keep it unchanged.
- If id is even → swap with previous (id - 1).
- COUNT(*) helps identify last row.

Approach 2 (Window Functions):
- LEAD() gets next row's student.
- LAG() gets previous row's student.
- For odd rows → take next student.
- For even rows → take previous student.
- If no next row (last row), keep original.

Why it works:
- IDs are continuous, so pairing is predictable.
- CASE handles conditional remapping cleanly.
- Window functions simplify neighbor access.

Time Complexity:
- O(n) → full table scan

Space Complexity:
- O(1) (logical transformation, no extra storage)

Key SQL concepts:
- CASE WHEN
- Modulo operator (id % 2)
- Subquery (COUNT)
- Window functions (LEAD, LAG)
- ORDER BY