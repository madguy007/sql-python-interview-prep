-- Step 1: Find each customer's last transaction date
WITH customer_last_transaction AS (
    SELECT
        customer_id,
        MAX(transaction_date) AS last_transaction_date
    FROM transactions
    GROUP BY customer_id
),

-- Step 2: Identify churned customers
-- Churn Definition:
-- Customer has not transacted for the next 6 months
churned_customers AS (
    SELECT
        customer_id,
        last_transaction_date,
        MONTH(last_transaction_date) AS churn_month,
        YEAR(last_transaction_date) AS churn_year
    FROM customer_last_transaction
    WHERE last_transaction_date <= DATE_SUB(NOW(), INTERVAL 6 MONTH)
)

-- Step 3: Calculate monthly churn count
SELECT
    churn_year,
    churn_month,
    COUNT(DISTINCT customer_id) AS churned_customers
FROM churned_customers
GROUP BY churn_year, churn_month
ORDER BY churn_year, churn_month;