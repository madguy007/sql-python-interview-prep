# Insights – Median Salary Using Window Functions

## 1️⃣ Core Idea

The median represents the middle value when data is sorted in ascending order.

- If total rows are odd → one middle value
- If total rows are even → average of two middle values

SQL does not have a built-in universal MEDIAN function, so we compute it manually.

---

## 2️⃣ Step 1 – Assign Row Numbers

ROW_NUMBER() OVER (ORDER BY salary)

This assigns position numbers after sorting salaries.

Example:

Salary | rn
10     | 1
20     | 2
30     | 3
40     | 4
50     | 5

---

## 3️⃣ Step 2 – Count Total Rows

COUNT(*) OVER ()

This gives total number of rows on every row.

Example:
If there are 5 rows → total_count = 5 on every row.

---

## 4️⃣ Step 3 – Identify Middle Position(s)

Middle index formula:

(total_count + 1) / 2

If total_count is odd (5):
(5 + 1) / 2 = 3 → select row 3

If total_count is even (4):
(4 + 1) / 2 = 2.5

We use:
FLOOR(2.5) = 2
CEIL(2.5) = 3

So rows 2 and 3 are selected.

---

## 5️⃣ Why AVG() Is Used

If odd:
Both FLOOR and CEIL give same value → one row → AVG returns that value.

If even:
Two rows selected → AVG returns correct median.

---

## 6️⃣ Concepts Tested

- Window functions
- Position-based filtering
- Mathematical reasoning in SQL
- Handling even vs odd datasets
- Dynamic calculation without hardcoding

---

## 7️⃣ Why This Is Interview-Level

This problem tests:
- Whether you understand row positioning
- Whether you can convert mathematical logic into SQL
- Whether you understand window functions deeply

Median questions often separate intermediate SQL users from advanced-level candidates.
