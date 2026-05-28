SELECT category, product, total_spend
FROM (
    SELECT
        category,
        product,
        SUM(spend) AS total_spend,
        ROW_NUMBER() OVER(
            PARTITION BY category
            ORDER BY SUM(spend) DESC
        ) AS rn
    FROM product_spend
    WHERE EXTRACT(YEAR FROM transaction_date) = 2022
    GROUP BY category, product
) t
WHERE rn <= 2;

==================================================