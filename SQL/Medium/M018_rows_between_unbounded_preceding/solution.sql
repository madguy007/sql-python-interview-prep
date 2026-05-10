WITH daily_sale AS (
    SELECT 
        visited_on,
        SUM(amount) AS day_amount
    FROM customer
    GROUP BY visited_on
)

SELECT 
    visited_on,
    
    SUM(day_amount) OVER (
        ORDER BY visited_on 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    
    ROUND(
        AVG(day_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS average_amount

FROM daily_sale
LIMIT 1000000 OFFSET 6;