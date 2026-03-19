1. Core idea:
   - Acceptance rate = accepted_requests / total_requests
   - But we must count UNIQUE request pairs, not raw rows.

2. Why DISTINCT is critical:
   - Tables may contain duplicates
   - Example:
     → (3,4) appears twice in accepted table
     → Should be counted only once
   - So we use:
     → COUNT(DISTINCT sender_id, send_to_id) logic

3. SQLite limitation:
   - SQLite does not support COUNT(DISTINCT col1, col2)
   - So we combine columns:
     → sender_id || '-' || send_to_id

4. Why *1.0 is used:
   - Ensures floating point division
   - Otherwise integer division may truncate result

5. Join vs No Join:
   - Join approach explicitly matches requests with accepted
   - But simpler approach:
     → count both independently and divide

6. Important interview pattern:
   - When problem asks for "rate":
     → numerator and denominator often come from separate aggregations
     → compute them independently

7. Rounding:
   - Use ROUND(value, 2) for 2 decimal precision

8. Key takeaway:
   - Always check for duplicates
   - Always clarify if counting rows or unique entities