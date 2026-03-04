-- Detect price increases compared to previous update

WITH price_changes AS (
    SELECT
        product_id,
        update_date,
        price,
        CASE
            WHEN price > LAG(price) OVER (
                PARTITION BY product_id
                ORDER BY update_date
            )
            THEN 1 ELSE 0
        END AS inc
    FROM ProductPrices
),

-- Create groups for consecutive increase streaks
grp AS (
    SELECT
        product_id,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY update_date
        )
        -
        ROW_NUMBER() OVER (
            PARTITION BY product_id, inc
            ORDER BY update_date
        ) AS g
    FROM price_changes
    WHERE inc = 1
)

-- Identify products with at least 2 consecutive increases
SELECT product_id
FROM grp
GROUP BY product_id, g
HAVING COUNT(*) >= 2;
