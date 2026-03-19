-- Approach 1: Using DISTINCT + scalar subqueries (Recommended)
SELECT 
    ROUND(
        (
            SELECT COUNT(DISTINCT requester_id || '-' || accepter_id)
            FROM request_accepted
        ) * 1.0
        /
        (
            SELECT COUNT(DISTINCT sender_id || '-' || send_to_id)
            FROM friend_request
        ),
    2) AS acceptance_rate;

-- Approach 2: Using LEFT JOIN (explicit matching)
SELECT 
    ROUND(
        COUNT(DISTINCT r.requester_id || '-' || r.accepter_id) * 1.0
        /
        COUNT(DISTINCT f.sender_id || '-' || f.send_to_id),
    2) AS acceptance_rate
FROM friend_request f
LEFT JOIN request_accepted r
    ON f.sender_id = r.requester_id
   AND f.send_to_id = r.accepter_id;

-- Approach 3: Using CTE (clean structure)
WITH req AS (
    SELECT COUNT(DISTINCT sender_id || '-' || send_to_id) AS total_req
    FROM friend_request
),
acc AS (
    SELECT COUNT(DISTINCT requester_id || '-' || accepter_id) AS total_acc
    FROM request_accepted
)
SELECT ROUND(total_acc * 1.0 / total_req, 2) AS acceptance_rate
FROM req, acc;