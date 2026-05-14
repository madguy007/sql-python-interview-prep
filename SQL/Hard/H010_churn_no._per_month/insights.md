- Customer churn means customers who were previously active but stopped transacting.
- In this case:
  Churn = No transactions for 6 consecutive months after their last purchase.

Important Rule:
- Churn is based on customer lifecycle inactivity.
- It is NOT simply customers inactive during one month.

==================================================
Step-by-Step SQL Logic
==================================================

1. Find Customer's Last Transaction
- Use:
  MAX(transaction_date)

Purpose:
- Determines final customer activity date

Example:
MAX(transaction_date)

--------------------------------------------------

2. Define Churn
- If customer’s last transaction is older than 6 months:
  Customer is churned

Example:
WHERE last_transaction_date <= DATE_SUB(NOW(), INTERVAL 6 MONTH)

--------------------------------------------------

3. Monthly Churn Trend
- Group churned customers by:
  YEAR(last_transaction_date)
  MONTH(last_transaction_date)

Purpose:
- Tracks when customers became inactive permanently

--------------------------------------------------

4. Count Churned Customers
- Use:
  COUNT(DISTINCT customer_id)

Purpose:
- Monthly churn volume

==================================================
Key SQL Concepts
==================================================

- MAX()
- DATE_SUB()
- COUNT(DISTINCT)
- CTE
- GROUP BY
- ORDER BY
- Customer lifecycle analysis

==================================================
Interview Memory Rules
==================================================

Find customer’s final activity?
→ MAX(transaction_date)

Define churn?
→ No activity for defined retention window

Monthly churn trend?
→ Group by last active month

Count churned customers?
→ COUNT(DISTINCT customer_id)

==================================================
Core Business Insight
==================================================

Monthly churn trend helps businesses:
- Track retention decline
- Identify risky months
- Forecast revenue loss
- Improve customer retention strategy

Strong churn analysis improves:
- Customer retention
- Revenue forecasting
- Product strategy
- SQL interview readiness