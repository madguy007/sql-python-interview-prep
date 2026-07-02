# Insights

### Common SQL Mistake: `= NULL`

A common mistake is trying to compare NULL values using `=`.

Example of incorrect query:

CASE
WHEN n.npv = NULL THEN 0
ELSE n.npv
END

This does **not work** because in SQL **NULL cannot be compared using `=`**.

SQL follows **three-valued logic**:
- TRUE
- FALSE
- UNKNOWN

Any comparison with NULL results in **UNKNOWN**, not TRUE.

Example:

SELECT NULL = NULL;

Result → UNKNOWN

Therefore the condition never becomes TRUE.

---

### Correct Way to Check NULL

Use `IS NULL` instead.

CASE
WHEN n.npv IS NULL THEN 0
ELSE n.npv
END

---

### Cleaner Solution Using `COALESCE`

`COALESCE()` returns the first non-NULL value.

COALESCE(n.npv, 0)

Meaning:
- If `n.npv` is NULL → return `0`
- Otherwise → return `n.npv`
