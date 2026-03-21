Number of Customer Plans After Free Trial

You are given two tables:

Table: plans  
- plan_id  
- plan_name  

Table: subscriptions  
- customer_id  
- plan_id  
- start_date  

Each row represents a customer subscribing to a plan on a given date.

Assume:
- plan_id = 0 represents the free trial
- Customers can move from free trial to a paid plan

Task:
Find the number and percentage of customer plans chosen AFTER their initial free trial.

Output:
- next_plan (plan chosen after free trial)
- conversions (number of customers who moved to that plan)
- conversion_percentage