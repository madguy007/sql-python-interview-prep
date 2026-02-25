
# Insight

This problem is about a **cross-product based join**, not a relationship join.

The question only says:
"Find customers and salesmen who live in the same city."

It does NOT say:
"Find customers with their assigned salesman."

So we should NOT use:
c.salesman_id = s.salesman_id

Instead, we match purely on city:

s.city = c.city

This means:
- Every customer is compared with every salesman.
- Only rows where both live in the same city are returned.
- Assignment relationship is irrelevant here.

Key Learning:
Do not assume foreign key relationships unless the question explicitly asks for them.
Always translate the English requirement directly into the JOIN condition.
