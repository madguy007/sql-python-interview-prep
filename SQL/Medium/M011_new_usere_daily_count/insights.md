1. Core problem:
   - We are NOT counting all login events.
   - We are counting users who logged in for the FIRST time.

2. Key rule (VERY IMPORTANT for interviews):
   - Whenever a question mentions "first login", "first purchase", "first event":
     → ALWAYS use MIN(date) per user
   - This ensures only the earliest occurrence is selected.

3. Why your initial approach failed:
   - You filtered activity = 'login' but still had multiple login rows per user.
   - This leads to duplicate counting.

4. Example (user_id = 5 case):
   - 2019-03-01 → login
   - 2019-06-21 → login
   - Your query counts BOTH dates ❌
   - Correct logic:
     → MIN(activity_date) = 2019-03-01
     → Only this date should be considered ✅
     → 2019-06-21 is ignored

5. How we fixed it:
   - GROUP BY user_id
   - MIN(activity_date) gives first login per user
   - Now each user appears only once → no double counting

6. Why filtering is done AFTER aggregation:
   - If you filter before finding MIN, you may remove the true first login
   - So:
     Step 1 → find first login
     Step 2 → apply date filter

7. Key SQL concepts used:
   - GROUP BY for user-level aggregation
   - MIN() to find first occurrence
   - Subquery to separate logic layers
   - Window function (ROW_NUMBER) as alternative