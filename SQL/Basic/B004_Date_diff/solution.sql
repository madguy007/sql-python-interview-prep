-- Calculate subscription duration in days

SELECT 
    id,
    CAST(julianday(EndDate) - julianday(StartDate) AS INTEGER) AS SubscriptionDays
FROM Subscriptions;
