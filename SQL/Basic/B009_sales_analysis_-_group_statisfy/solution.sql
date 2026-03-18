-- Approach 1: Using MIN and MAX (Recommended)
SELECT product_id
FROM Sales
GROUP BY product_id
HAVING 
    MIN(sale_date) >= '2019-01-01'
    AND MAX(sale_date) <= '2019-03-31';

-- Approach 2: Using CASE to explicitly remove products with out-of-range sales
SELECT product_id
FROM Sales
GROUP BY product_id
HAVING 
    SUM(CASE 
        WHEN sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31' 
        THEN 1 ELSE 0 
    END) = 0;

-- Approach 3: Using NOT EXISTS
SELECT DISTINCT s1.product_id
FROM Sales s1
WHERE NOT EXISTS (
    SELECT 1
    FROM Sales s2
    WHERE s1.product_id = s2.product_id
      AND s2.sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
);