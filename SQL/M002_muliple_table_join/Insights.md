# Insight

## 🔎 Logical Thinking

Step 1:
Start from `orders` because the question says:
"salespeople who generated orders".

Step 2:
For each order,
- Go to `customer` → get customer city
- Go to `salesman` → get salesman city

Step 3:
Compare both cities.
If cities are different → return the row.

So logically:
Order → Customer → Salesman → Compare city

---

## ✅ Converting Logic into INNER JOIN

Relationship first, then filter:

SELECT ...
FROM orders o
JOIN customer c
  ON o.customer_id = c.customer_id
JOIN salesman s
  ON o.salesman_id = s.salesman_id
WHERE c.city <> s.city;

INNER JOIN directly connects only relevant rows.

---

## 🔁 Converting Logic into Cross Join (Old Syntax)

FROM orders o, customer c, salesman s
WHERE o.customer_id = c.customer_id
AND o.salesman_id = s.salesman_id
AND c.city <> s.city;

Here:
1. All tables are cross joined first.
2. WHERE clause filters matching relationships.
3. Then city condition is applied.

---

## 🎯 Key Difference

INNER JOIN → filters while joining  
Cross Join + WHERE → joins everything first, then filters  

Final result is the same.
